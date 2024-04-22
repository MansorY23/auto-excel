import pandas as pd
from services.categories import categories_diesel, \
    categories_petrol
from pathlib import Path
from typing import Union
import logging
from datetime import date

pd.options.mode.chained_assignment = None


def process_diesel(
        daily_excel_path: Union[Path, str]) -> pd.DataFrame:
    try:
        first_df = pd.read_excel(io=daily_excel_path, engine="calamine",
                                 header=None,
                                 skiprows=10, usecols=[0, 3],
                                 names=["item", "number"]
                                 )
    except FileNotFoundError as e:
        raise FileNotFoundError(f"В директории нет ежедневного отчёта за сегодняшнее число\n"
                                f"Ошибка: {e}")
    all_diesel_series = first_df["number"].loc[first_df["item"] == "Дизтопливо (кг.)"]
    all_diesel = int(all_diesel_series.iloc[0])

    first_df = first_df.loc[all_diesel_series.index[0]:]
    df_without_nums = first_df[first_df["item"].isin(categories_diesel.keys())]

    # регулярка, чтобы забирать только складские номера машин
    df_without_duplicates = first_df[~first_df["item"].str.match("(\d{2}).(\d{2}).(\d{4}) (\d{1,2}):(\d{2}):(\d{2})")]
    updated_df = df_without_duplicates[df_without_duplicates["item"].str.match("\d{5} ")]
    updated_df["item"] = [i[:5] for i in updated_df["item"]]

    df = pd.concat([df_without_nums, updated_df])
    # добавляю индекс, т.к excel приходит кривой
    df["index_column"] = range(1, len(df) + 1)
    df = df.set_index("index_column")

    group_df = df.set_index("item").groupby(categories_diesel)
    agg_df = group_df.sum().reset_index()
    # переменная для сравнения сходятся ли данные
    all_diesel_after_agg = int(agg_df["number"].sum())

    if int(all_diesel) != int(all_diesel_after_agg):
        raise ValueError("Значения по дизелю не сходятся. Возможно появилась новая техника \n"
                         f"Весь дизель: {all_diesel}, Подсчитанный дизель: {all_diesel_after_agg}"
                         f"{undefined_rows(updated_df, 'diesel')}")

    else:
        logging.info("Значения дизеля сходятся. Дизель подсчитан верно")

    agg_df = agg_df.rename(columns={"item": "Группа",
                                    "number": str(date.today().day)})
    return agg_df


def process_petrol(
        daily_excel_path: Union[Path, str]) -> pd.DataFrame:
    try:
        first_df = pd.read_excel(io=daily_excel_path, engine="calamine",
                                 header=None,
                                 skiprows=10, usecols=[0, 3],
                                 names=["item", "number"]
                                 )
    except FileNotFoundError as e:
        raise FileNotFoundError(f"В директории нет ежедневного отчёта за сегодняшнее число\n"
                                f"Ошибка: {e}")

    all_petrol_series = first_df["number"].loc[first_df["item"] ==
                                            "Бензин автомобильный АИ-92-К5 ГОСТ 32513-2013"]
    all_petrol = int(all_petrol_series.iloc[0])
    diesel_index = first_df["number"].loc[first_df["item"] ==
                                            "Дизтопливо (кг.)"]

    first_df = first_df.loc[all_petrol_series.index[0]:diesel_index.index[0]]
    # сначала забираем значения, у которых нет складского номера
    df_without_nums = first_df[first_df.item.isin(categories_petrol.keys())]

    # регулярка, чтобы забирать только складские номера машин
    df_without_duplicates = first_df[~first_df["item"].str.match("(\d{2}).(\d{2}).(\d{4}) (\d{1,2}):(\d{2}):(\d{2})")]
    updated_df = df_without_duplicates[df_without_duplicates["item"].str.match("\d{5} ")]
    updated_df["item"] = [i[:5] for i in updated_df["item"]]

    df = pd.concat([df_without_nums, updated_df])

    # добавляю индекс, т.к excel приходит кривой
    df["index_column"] = range(1, len(df) + 1)
    df = df.set_index("index_column")

    group_df = df.set_index("item").groupby(categories_petrol)
    agg_df = group_df.sum().reset_index()
    # переменная для сравнения сходятся ли данные
    all_petrol_after_agg = int(agg_df["number"].sum())

    if int(all_petrol) != int(all_petrol_after_agg):
        raise ValueError("Значения по бензину не сходятся. Возможно появилась новая техника \n"
                         f"весь бензин: {all_petrol}, подсчитанный бензин: {all_petrol_after_agg}\n"
                         f"{undefined_rows(updated_df, 'petrol')}")
    else:
        logging.info("Значения бензина сходятся. Бензин подсчитан верно")

    agg_df = agg_df.rename(columns={"item": "Группа",
                                    "number": str(date.today().day)})

    return agg_df


def undefined_rows(df: pd.DataFrame,
                   type: str) -> str:
    if type == "diesel":
        machinery_with_plate = df[~df.item.isin(categories_diesel.keys())]
        print(machinery_with_plate)
        # return f"В словаре Дизеля не хватает техники с хоз.номером: {machinery_with_plate['item'].item()}\n" \
        #       f"Добавьте её в файл services/categories.py"

    if type == "petrol":
        machinery_with_plate = df[~df.item.isin(categories_petrol.keys())]
        print(machinery_with_plate)
        # return f"В словаре бензина не хватает техники с хоз.номером: {machinery_with_plate['item']}\n" \
        #       f"Добавьте её в файл services/categories.py"
