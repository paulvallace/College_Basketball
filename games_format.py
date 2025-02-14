import pandas as pd

# Read data
df = pd.read_csv('historical data/Past Games/game_results_2025-02-10_2025-02-12.csv')  # Update filename as needed
df = df.dropna()

  
if 'Team' in df.columns:
    df['Team'] = df['Team'].str.replace("St.", "St").str.replace("'", "").str.replace("Boston College", "Boston Col").str.replace(
    "TCU", "TX Christian").str.replace("N.C.", "NC").str.replace("North Carolina", "N Carolina").str.replace(
    "South Carolina", "S Carolina").str.replace("West Virginia", "W Virginia").str.replace("Virginia Tech", "VA Tech").str.replace(
    "Miami FL", "Miami").str.replace("McNeese", "McNeese St").str.replace("Mississippi St", "Miss State").str.replace("SMU", "S Methodist")

if 'Opponent' in df.columns:
    df['Opponent'] = df['Opponent'].str.replace("St.", "St").str.replace("'", "").str.replace("Boston College", "Boston Col").str.replace(
    "TCU", "TX Christian").str.replace("N.C.", "NC").str.replace("North Carolina", "N Carolina").str.replace(
    "South Carolina", "S Carolina").str.replace("West Virginia", "W Virginia").str.replace("Virginia Tech", "VA Tech").str.replace(
    "Miami FL", "Miami").str.replace("McNeese", "McNeese St").str.replace("Mississippi St", "Miss State").str.replace("SMU", "S Methodist")

# Save to new file
df.to_csv('/Users/PaulVallace/Desktop/College Basketball/historical data/Past Games/game_results_2025-02-10_2025-02-12.csv', index=False)
