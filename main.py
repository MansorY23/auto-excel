from excel import excel_process, save_excel


def main():
    df = excel_process("dt_02.03.2024.xls")
    save_excel(df, "output_test.xlsx")


if __name__ == "__main__":
    main()