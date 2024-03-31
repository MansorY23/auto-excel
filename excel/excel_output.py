import pandas as pd
from typing import Union
from pathlib import Path
from datetime import date
import logging


def df_work():
    pass


def update_excel(daily_excel: pd.DataFrame,
                 path: Union[Path, str]) -> pd.DataFrame:

    today = date.today().day
    monthly_excel = pd.read_excel(path, skiprows=1,
                          sheet_name="ДТ")

    monthly_excel = monthly_excel.dropna(subset=["Группа"])
    merged_excel = monthly_excel.merge(daily_excel, on="Группа", how="left")
    merged_excel[today] = merged_excel[today].fillna(merged_excel[str(today)])
    merged_excel = merged_excel.drop([str(today)], axis=1)
    updated_excel = merged_excel.set_index("Группа")
    updated_excel.loc["расход энергопрогноз".upper()] = daily_excel.sum(numeric_only=True, axis=0)

    with pd.ExcelWriter(path, mode="a", engine='openpyxl',

                        if_sheet_exists='overlay') as writer:
        updated_excel.to_excel(writer, sheet_name='ДТ', startrow=1, startcol=0)
        logging.info("Excel successfully updated and saved")

    return updated_excel
