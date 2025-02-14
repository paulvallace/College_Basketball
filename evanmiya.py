import pandas as pd

def evanmiya_clean(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.dropna()
    
    df = df.drop(columns=['rank', 'tooltip_team', 'rank_inj', 'roster_rank', 'wins', 'losses', 'color_O', 'color_D',
                      'color_Diff', 'color_str_Diff', 'color_tempo_Diff', 'tooltip_str_Diff', 'tooltip_tempo_Diff'], errors='ignore')


    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii') if isinstance(x, str) else x)
    
    if "team" in df.columns:
        df["team"] = df["team"].str.replace("Saint", "St").str.replace("'", "").str.replace("Boston College", "Boston Col").str.replace(
        "TCU", "TX Christian").str.replace("N.C State", "NC State").str.replace("North Carolina", "N Carolina").str.replace(
        "South Carolina", "S Carolina").str.replace("West Virginia", "W Virginia").str.replace("Virginia Tech", "VA Tech").str.replace(
            "Miami FL", "Miami").str.replace("State", "St").str.replace("McNeese", "McNeese St").str.replace("Mississippi St", "Miss State").str.replace(
                "Ole Miss", "Mississippi").str.replace("SMU", "S Methodist")

    df.to_csv(output_file, index=False, header=True)

# Usage
evanmiya_clean("/Users/PaulVallace/Desktop/College Basketball/historical data/Kill Shot/evanmiya/evanmiya.csv", "/Users/PaulVallace/Desktop/College Basketball/historical data/Kill Shot/evanmiya/evanmiya_feb_10th.csv")