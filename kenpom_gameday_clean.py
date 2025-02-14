import pandas as pd

def kenpom_clean(input_file, output_file):
    try:
        df = pd.read_excel(input_file)
        df = df.dropna()
        
        if 'Team' in df.columns:
            df['Team'] = df['Team'].str.replace("St.", "St").str.replace("'", "").str.replace("Boston College", "Boston Col").str.replace(
                "TCU", "TX Christian").str.replace("N.C.", "NC").str.replace("North Carolina", "N Carolina").str.replace(
                "South Carolina", "S Carolina").str.replace("West Virginia", "W Virginia").str.replace("Virginia Tech", "VA Tech").str.replace(
                "Miami FL", "Miami").str.replace("McNeese", "McNeese St").str.replace("Mississippi St", "Miss State").str.replace("SMU", "S Methodist")
        
        df.to_csv(output_file, index=False, header=True, sep=" ")
        print(f"File successfully saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

# Usage
kenpom_clean("/Users/PaulVallace/Desktop/College Basketball/historical data/Kenpom/Kenpom Gameday/kenpom_2025-02-12_2025-02-12.xlsx", "/Users/PaulVallace/Desktop/College Basketball/historical data/Kenpom/Kenpom Gameday/kenpom_2025-02-12_2025-02-12.csv")
