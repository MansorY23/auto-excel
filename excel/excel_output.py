import pandas as pd
from openpyxl import load_workbook
from typing import Union
from pathlib import Path
from datetime import date


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
