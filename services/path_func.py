import datetime
from pathlib import Path
import os
from typing import Union


def monthly_excel_name(
        folder_path: Union[Path, str]) -> Path:
    today = datetime.date.today()

    return Path(f"{folder_path}/{today.strftime('%B_%Y')}GSM.xlsx")


def daily_excel_name(
        folder_path: Union[Path, str]) -> Path:
    today = datetime.date.today()

    return Path(f"{folder_path}/dt_{today.strftime('%d.%m.%Y')}.xls")


# get user name
# print(os.getenv('username'))
#print(monthly_excel_name(f"C:/Users/{os.getenv('username')}/Desktop/DT2024/GSM_AMT/"))
