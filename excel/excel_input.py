import pandas as pd
from .categories import categories
from pathlib import Path
from typing import Union
import logging

def excel_process(
        path: Union[Path, str]) -> pd.DataFrame:

    df = pd.read_excel(io=path, engine="calamine", header=None,
                       skiprows=10, usecols=[0, 3, 6 ],
                       names=["item", "number", "volume"]
                       )
    all_fuel = df["number"].loc[0]
    print(all_fuel)
    # регулярка, чтобы забирать только складские номера машин
    df = df[~df["item"].str.match("(\d{2}).(\d{2}).(\d{4}) (\d{1,2}):(\d{2}):(\d{2})")]
    df = df[df["item"].str.match("\d{5} ")]

    # добавляю индекс, т.к excel приходит кривой
    df["index_column"] = range(1, len(df)+1)
    df = df.set_index("index_column")

    df["item"] = [i[:5] for i in df["item"]]
    df = df.set_index("item").groupby(categories).sum()

    # переменная для сравнения сходятся ли данные
    all_fuel_after_agg = df["number"].sum()

    if all_fuel != all_fuel_after_agg:
        logging.error("Значения не сходятся. Возможно появился новый транспорт")
        raise ValueError("Значения не сходятся. Возможно появился новый транспорт")
    #print(df)
    return df


excel_process("dt_02.03.2024.xls")