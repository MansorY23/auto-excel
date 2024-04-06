import datetime
from pathlib import Path
import os
from typing import Union


def monthly_excel_name(
        folder_path: Union[Path, str]) -> str:
    today = datetime.date.today()
    monthly_excel_path = f"{folder_path}" \
                         f"DT_{today.year}/" \
                         f"{today.strftime('%m_%B')}/" \
                         f"{today.strftime('%B_%Y')}GSM.xlsx"

    return monthly_excel_path


def daily_excel_name(
        folder_path: Union[Path, str]) -> str:
    today = datetime.date.today()
    daily_excel_path = f"{folder_path}" \
                       f"DT_{today.year}/" \
                       f"{today.strftime('%m_%B')}/" \
                       f"dt_{today.strftime('%d.%m.%Y')}.xls"

    return daily_excel_path


# get user name
# print(os.getenv('username'))
print(monthly_excel_name(f"C:/Users/{os.getenv('username')}/Desktop/DT2024/GSM_AMT/"))
