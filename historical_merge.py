import pandas as pd

def merge_excel_sheets(file1_path, file2_path, output_path):
    # Read both Excel files
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)
    
    # Concatenate the dataframes
    merged_df = pd.concat([df1, df2], ignore_index=True)
    
    # Write to a new Excel file
    merged_df.to_excel(output_path, index=False)
    print(f"Merged file saved to: {output_path}")

# Example usage
file1_path = '/Users/PaulVallace/Desktop/College Basketball/historical data/Kenpom/historical_kenpom.xlsx'
file2_path = '/Users/PaulVallace/Desktop/College Basketball/historical data/Kenpom/kenpom_2025-02-11_2025-02-13.xlsx'
output_path = "/Users/PaulVallace/Desktop/College Basketball/historical data/Kenpom/historical_kenpom.xlsx"

merge_excel_sheets(file1_path, file2_path, output_path)