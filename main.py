from excel import excel_process, update_excel
from outlook import save_attachments
from dotenv import load_dotenv
from services import daily_excel_name, monthly_excel_name
import os
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    daily_excel_path = save_attachments(os.environ["SUBJECT"],
                                        daily_excel_name(os.environ['EXCEL_PATH']),
                                        ".xls", os.environ["INBOX_ITEM"])

    daily_excel_df = excel_process(daily_excel_path)
    update_excel(daily_excel_df,
                 monthly_excel_name(os.environ["EXCEL_PATH"]))

    return None


if __name__ == "__main__":
    main()
