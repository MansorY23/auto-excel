from excel import excel_work, save_excel


def main():
    df = excel_work()
    save_excel(df)


if __name__ == "__main__":
    main()