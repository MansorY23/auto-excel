import pandas as pd
from categories import categories
from pathlib import Path
from typing import Union
import logging
from openpyxl import load_workbook
from datetime import date


def excel_process(
        path: Union[Path, str]) -> pd.DataFrame:
    df = pd.read_excel(io=path, engine="calamine", header=None,
                       skiprows=10, usecols=[0, 3],
                       names=["item", "number"]
                       )

    all_fuel = df["number"].loc[df["item"] == "Заправка"].sum()

    # регулярка, чтобы забирать только складские номера машин
    df = df[~df["item"].str.match("(\d{2}).(\d{2}).(\d{4}) (\d{1,2}):(\d{2}):(\d{2})")]
    df = df[df["item"].str.match("\d{5} ")]

    # добавляю индекс, т.к excel приходит кривой
    df["index_column"] = range(1, len(df) + 1)
    df = df.set_index("index_column")

    df["item"] = [i[:5] for i in df["item"]]
    df = df.set_index("item").groupby(categories).sum().reset_index()
    # переменная для сравнения сходятся ли данные
    all_fuel_after_agg = df["number"].sum()
    if int(all_fuel) != int(all_fuel_after_agg):
        logging.error("Значения не сходятся. Возможно появился новый транспорт")
        raise ValueError("Значения не сходятся. Возможно появился новый транспорт")
    df = df.rename(columns={"item": "Группа",
                            "number": str(date.today().day)})
    return df


def update_excel(df: pd.DataFrame,
                 path: Union[Path, str]):
    today = date.today().day
    excel = pd.read_excel(path, skiprows=1,
                          sheet_name="ДТ")
                          #names=["Группа", "1", "2", "3", "4", "5",
                           #      "6", "7", "8", "9", "10", "11",
                            #     "12", "13", "14", "15", "16",
                             #    "17", "18", "19", "20", "21", "22",
                              #   "23", "24", "25", "26", "27", "28",
                               #  "29", "30", "31"])
    excel = excel.dropna(subset=["Группа"])
    excel = excel.merge(df, on="Группа", how="left")
    excel[today] = excel[today].fillna(excel[str(today)])
    excel = excel.drop([str(today)], axis=1)
    excel = excel.set_index("Группа")

    with pd.ExcelWriter(path, mode="a", engine='openpyxl',
                        if_sheet_exists='overlay') as writer:
        print(excel)
        excel.to_excel(writer, sheet_name='ДТ', startrow=1, startcol=0)

    return excel


def write_to_excel(df: pd.DataFrame,
                   path: Union[Path, str],
                   worksheet:str):
    wb = load_workbook(path)
    ws = wb[worksheet]

    for row in range(0, df.shape[0]):
        for col in range(0, date.today().day):
            print(row, col)
    wb.save(path)
    return None


#output_excel(excel_process("dt_02.03.2024.xls"), "output_example.xlsx")
update_excel(excel_process("dt_02.03.2024.xls"), "output_perfect.xlsx")
#write_to_excel(update_excel(excel_process("dt_02.03.2024.xls"),
#                            "ideal_output.xlsx"),
#               "ideal_output.xlsx", "ДТ")
