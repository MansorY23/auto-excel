import pandas as pd
from typing import Union
from pathlib import Path
from datetime import date
import logging


def update_diesel(daily_excel: pd.DataFrame,
                  monthly_excel_path: Union[Path, str]) -> pd.DataFrame:
    today = date.today().day
    try:
        monthly_excel = pd.read_excel(monthly_excel_path,
                                      skiprows=1,
                                      sheet_name="ДТ")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"В директории нет месячного отчёта за сегодняшнее число\n"
                                f"Ошибка: {e}")

    monthly_excel = monthly_excel.dropna(subset=["Группа"])
    merged_excel = monthly_excel.merge(daily_excel, on="Группа", how="left")
    merged_excel[today] = merged_excel[str(today)]
    merged_excel = merged_excel.drop([str(today)], axis=1)
    updated_excel = merged_excel.set_index("Группа")

    updated_excel.loc["расход энергопрогноз".upper(), today] = \
        updated_excel[today].iloc[[0, 1]].sum()

    updated_excel.loc["расход аметистовое".upper(), today] = \
        updated_excel.loc['Буровые станки "ROC"': 'Насосы Godwin', today].sum()

    updated_excel.loc["ИТОГО - суточный расход", today] = \
        updated_excel[today].loc[["расход аметистовое".upper(), "расход энергопрогноз".upper()]].sum()

    with pd.ExcelWriter(monthly_excel_path,
                        mode="a", engine='openpyxl',
                        if_sheet_exists='overlay') as writer:
        updated_excel.to_excel(writer, sheet_name='ДТ', startrow=1, startcol=0)
        logging.info(f"Лист с Дизельным топливом на {today} число обновлён")

    return updated_excel


def update_petrol(daily_excel: pd.DataFrame,
                  monthly_excel_path: Union[Path, str]) -> pd.DataFrame:
    today = date.today().day
    try:
        monthly_excel = pd.read_excel(monthly_excel_path,
                                      skiprows=1,
                                      sheet_name="БЕНЗИН")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"В директории нет месячного отчёта за сегодняшнее число\n"
                                f"Ошибка: {e}")

    monthly_excel = monthly_excel.dropna(subset=["Группа"])
    merged_excel = monthly_excel.merge(daily_excel, on="Группа", how="left")
    merged_excel[today] = merged_excel[str(today)]

    merged_excel = merged_excel.drop([str(today)], axis=1)
    updated_excel = merged_excel.set_index("Группа")

    updated_excel.loc["ИТОГО - суточный расход", today] = \
        updated_excel.loc["12406 Автомобиль УАЗ Фермер(ПГР)": 'Бензин - прочие нужды', today].sum()

    with pd.ExcelWriter(monthly_excel_path,
                        mode="a", engine='openpyxl',
                        if_sheet_exists='overlay') as writer:
        updated_excel.to_excel(writer, sheet_name='БЕНЗИН', startrow=1, startcol=0)
        logging.info(f"Лист с Бензином на {today} число обновлён")

    return updated_excel
