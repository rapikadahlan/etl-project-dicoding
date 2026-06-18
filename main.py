from utils.extract import scrape_all
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_sheets, save_to_postgres

SPREADSHEET_ID = "1V2EcRs0n-OP7MNixN7UIf42ZqffgBD4oQGKPKx7gdY0"


def main():
    raw_data = scrape_all()
    df = transform_data(raw_data)

    print(df.info())

    save_to_csv(df)
    save_to_sheets(df, SPREADSHEET_ID)
    save_to_postgres(df)


if __name__ == "__main__":
    main()