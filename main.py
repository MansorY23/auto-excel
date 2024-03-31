from excel import excel_process, update_excel
from outlook import save_attachments


def main():
    excel_path = save_attachments("ГСМ",
                                  r"C:\Users\ivanovko\Desktop\DT2024\GSM_AMT\DT_2024\03_march",
                                    ".xls", "ГСМ АМТ")

    df = excel_process(excel_path)
    update_excel(df, "output_test.xlsx")


if __name__ == "__main__":
    main()