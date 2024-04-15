from excel import (update_petrol,
                   update_diesel,
                   process_diesel,
                   process_petrol)
from outlook import save_attachments
from dotenv import load_dotenv
from services import (daily_excel_name,
                      monthly_excel_name,
                      create_montly_folder)
import os
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    #daily_excel_path = save_attachments(os.environ["SUBJECT"],
    #                    daily_excel_name(f"C:/Users/{os.getenv('username')}/Desktop/{os.environ['EXCEL_PATH']}"),
    #                                    ".xls", os.environ["INBOX_ITEM"])
    path = create_montly_folder()

    monthly_excel = monthly_excel_name(path)
    daily_excel = daily_excel_name(path)

    update_diesel(process_diesel(daily_excel), monthly_excel)
    update_petrol(process_petrol(daily_excel), monthly_excel)

    return None


if __name__ == "__main__":
    main()
