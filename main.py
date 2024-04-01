from excel import excel_process, update_excel
from outlook import save_attachments
from dotenv import load_dotenv
import os
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    #daily_excel_path = save_attachments(os.environ["SUBJECT"],
    #                                    f"{os.environ['DAILY_EXCEL_PATH']}\03_march",
    #                                    ".xls", os.environ["INBOX_ITEM"])

    daily_excel_df = excel_process(os.environ["DAILY_EXCEL_PATH"])
    update_excel(daily_excel_df, os.environ["MONTHLY_EXCEL_PATH"])

    return None

if __name__ == "__main__":
    main()
