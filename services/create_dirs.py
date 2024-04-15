import logging
from pathlib import Path
import os
from datetime import date


def create_montly_folder() -> Path:
    today = date.today()
    root_path = Path(f"C:/Users/{os.getenv('username')}/"
                     f"Desktop/DT{today.year}/"
                     f"GSM_AMT/DT_{today.year}/"
                     f"{today.strftime('%m_%B')}")

    if not os.path.exists(root_path):
        logging.info(f"Корневой папки DT_2024 не существует, создаю новую")
        root_path.mkdir(parents=True, exist_ok=True)
        print(root_path)

    return root_path

