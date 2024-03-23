import pandas as pd
from openpyxl import load_workbook
from typing import Union
from pathlib import Path


def save_excel(df: pd.DataFrame,
               path: Union[Path, str]) -> None:
    wb = load_workbook(path)
    ws = wb.active
    print(ws)
    wb.save("2024.xlsx")
    return None

