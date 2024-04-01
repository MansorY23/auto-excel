import pandas as pd
from services.categories import categories
from pathlib import Path
from typing import Union
import logging
from datetime import date


def excel_process(
        daily_excel_path: Union[Path, str]) -> pd.DataFrame:
    df = pd.read_excel(io=daily_excel_path, engine="calamine",
                       header=None,
                       skiprows=10, usecols=[0, 3],
                       names=["item", "number"]
                       )

    all_fuel = int(df["number"].loc[df["item"] == "Топливо"].iloc[0])
    df_without_nums = df[df.item.isin(categories.keys())]

    # регулярка, чтобы забирать только складские номера машин
    df = df[~df["item"].str.match("(\d{2}).(\d{2}).(\d{4}) (\d{1,2}):(\d{2}):(\d{2})")]
    df = df[df["item"].str.match("\d{5} ")]
    df["item"] = [i[:5] for i in df["item"]]

    df = pd.concat([df_without_nums, df])

    # добавляю индекс, т.к excel приходит кривой
    df["index_column"] = range(1, len(df) + 1)
    df = df.set_index("index_column")

    agg_df = df.set_index("item").groupby(categories).sum().reset_index()
    # переменная для сравнения сходятся ли данные
    all_fuel_after_agg = int(agg_df["number"].sum())

    if int(all_fuel) != int(all_fuel_after_agg):
        #print(df[df["item"].isin(categories.keys())])
        raise ValueError("Значения не сходятся. Возможно появился новый транспорт \n"
                         f"всё топливо: {all_fuel}, подсчитанное топливо: {all_fuel_after_agg}")
    else:
        logging.info("Значения сходятся. Табличка подсчитана верно")

    agg_df = agg_df.rename(columns={"item": "Группа",
                            "number": str(date.today().day)})
    return agg_df



