import pandas as pd
from services.categories import categories_diesel,\
    categories_petrol
from pathlib import Path
from typing import Union
import logging
from datetime import date


def process_diesel(
        daily_excel_path: Union[Path, str]) -> pd.DataFrame:
    try:
        df = pd.read_excel(io=daily_excel_path, engine="calamine",
                           header=None,
                           skiprows=10, usecols=[0, 3],
                           names=["item", "number"]
                           )
    except FileNotFoundError as e:
        raise FileNotFoundError(f"В директории нет ежедневного отчёта за сегодняшнее число\n"
                                f"Ошибка: {e}")

    all_diesel = int(df["number"].loc[df["item"] == "Дизтопливо (кг.)"].iloc[0])
    df_without_nums = df[df.item.isin(categories_diesel.keys())]

    # регулярка, чтобы забирать только складские номера машин
    df = df[~df["item"].str.match("(\d{2}).(\d{2}).(\d{4}) (\d{1,2}):(\d{2}):(\d{2})")]
    df = df[df["item"].str.match("\d{5} ")]
    df["item"] = [i[:5] for i in df["item"]]

    df = pd.concat([df_without_nums, df])

    # добавляю индекс, т.к excel приходит кривой
    df["index_column"] = range(1, len(df) + 1)
    df = df.set_index("index_column")

    agg_df = df.set_index("item").groupby(categories_diesel).sum().reset_index()
    # переменная для сравнения сходятся ли данные
    all_diesel_after_agg = int(agg_df["number"].sum())

    if int(all_diesel) != int(all_diesel_after_agg):
        raise ValueError("Значения не сходятся. Возможно появился новый транспорт \n"
                         f"весь дизель: {all_diesel}, подсчитаннный дизель: {all_diesel_after_agg}")
    else:
        logging.info("Значения дизеля сходятся. Дизель подсчитан верно")

    agg_df = agg_df.rename(columns={"item": "Группа",
                            "number": str(date.today().day)})
    return agg_df




def process_petrol(
        daily_excel_path: Union[Path, str]) -> pd.DataFrame:

    try:
        df = pd.read_excel(io=daily_excel_path, engine="calamine",
                           header=None,
                           skiprows=10, usecols=[0, 3],
                           names=["item", "number"]
                           )
    except FileNotFoundError as e:
        raise FileNotFoundError(f"В директории нет ежедневного отчёта за сегодняшнее число\n"
                                f"Ошибка: {e}")

    all_petrol = int(df["number"].loc[df["item"] == "Бензин АИ-92 (кг.)"].iloc[0])
    # сначала забираем значения, у которых нет складского номера
    df_without_nums = df[df.item.isin(categories_petrol.keys())]

    # регулярка, чтобы забирать только складские номера машин
    df = df[~df["item"].str.match("(\d{2}).(\d{2}).(\d{4}) (\d{1,2}):(\d{2}):(\d{2})")]
    df = df[df["item"].str.match("\d{5} ")]
    df["item"] = [i[:5] for i in df["item"]]

    df = pd.concat([df_without_nums, df])

    # добавляю индекс, т.к excel приходит кривой
    df["index_column"] = range(1, len(df) + 1)
    df = df.set_index("index_column")

    agg_df = df.set_index("item").groupby(categories_petrol).sum().reset_index()
    # переменная для сравнения сходятся ли данные
    all_petrol_after_agg = int(agg_df["number"].sum())

    if int(all_petrol) != int(all_petrol_after_agg):
        raise ValueError("Значения не сходятся. Возможно появился новый транспорт \n"
                         f"весь бензин: {all_petrol}, подсчитанный бензин: {all_petrol_after_agg}")
    else:
        logging.info("Значения бензина сходятся. Бензин подсчитан верно")

    agg_df = agg_df.rename(columns={"item": "Группа",
                            "number": str(date.today().day)})
                            
    return agg_df
