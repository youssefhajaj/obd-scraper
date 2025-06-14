import pandas as pd


def csv_to_excel(csv_file, excel_file):
    """
    Convert CSV file to Excel XLSX format

    Args:
        csv_file (str): Path to input CSV file
        excel_file (str): Path to output Excel file
    """
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Write to Excel file
    df.to_excel(excel_file, index=False, engine='openpyxl')

    print(f"Successfully converted {csv_file} to {excel_file}")


if __name__ == "__main__":
    # Input and output file paths
    input_csv = "obd_codes.csv"
    output_excel = "obd_codes.xlsx"

    # Perform conversion
    csv_to_excel(input_csv, output_excel)