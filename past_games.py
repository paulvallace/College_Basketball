import json
import csv
from datetime import datetime, timedelta
import requests
from typing import Dict, List, Tuple

def get_date_range(start_date_str: str, end_date_str: str) -> List[str]:
    """
    Generate a list of dates between start and end date.
    """
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    
    return date_list

def fetch_odds_data(date_str: str) -> dict:
    """
    Fetch game data from OddsShark API.
    """
    url = f"https://www.oddsshark.com/api/scores/ncaab/{date_str}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def format_date(timestamp: int) -> str:
    """
    Format timestamp to 'Feb 1st' format
    """
    date = datetime.fromtimestamp(timestamp)
    day = date.day
    suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10 if day not in [11, 12, 13] else 0, 'th')
    return date.strftime(f'%b {day}{suffix}')

def format_spread(home_spread: float, is_home_team: bool) -> str:
    """
    Format spread with proper sign.
    For home team: negative means favorite, positive means underdog
    For away team: opposite of home team's spread
    """
    if is_home_team:
        return f"{home_spread:+.1f}"
    else:
        return f"{-home_spread:+.1f}"

def process_games(data: dict) -> List[Dict]:
    """
    Process OddsShark JSON data and format game results with spread coverage.
    """
    formatted_games = []
    
    for game in data.get('scores', []):
        try:
            home_team = game['teams']['home']
            away_team = game['teams']['away']
            
            game_date = format_date(game['date'])
            
            # Get team names and scores
            home_name = home_team['names']['display_name']
            away_name = away_team['names']['display_name']
            home_score = home_team['score']
            away_score = away_team['score']
            
            # Get spread (from home team's perspective)
            home_spread = float(home_team['spread'])
            
            # Format spreads with signs for both teams
            home_spread_str = format_spread(home_spread, True)
            away_spread_str = format_spread(home_spread, False)
            
            # Calculate if spread was covered
            score_difference = home_score - away_score
            # For home team
            home_covered = 'Y' if score_difference > home_spread else 'N'
            if home_spread > 0:  # If home team is underdog
                home_covered = 'Y' if score_difference + home_spread > 0 else 'N'
            
            # For away team (opposite of home team)
            away_covered = 'Y' if home_covered == 'N' else 'N'
            
            # Create separate entries for home and away teams
            away_game = {
                'Team': away_name,
                'Opponent': home_name,
                'Team_Score': away_score,
                'Opp_Score': home_score,
                'Spread': away_spread_str,
                'Spread_Covered': away_covered,
                'Final_Score': f"{away_score}-{home_score}",
                'Date': game_date
            }
            
            home_game = {
                'Team': home_name,
                'Opponent': away_name,
                'Team_Score': home_score,
                'Opp_Score': away_score,
                'Spread': home_spread_str,
                'Spread_Covered': home_covered,
                'Final_Score': f"{home_score}-{away_score}",
                'Date': game_date
            }
            
            formatted_games.extend([away_game, home_game])
            
        except (KeyError, TypeError) as e:
            print(f"Error processing game: {str(e)}")
            continue
    
    return formatted_games

def save_to_csv(games: List[Dict], output_file: str):
    """
    Save game results to a CSV file.
    """
    if not games:
        raise ValueError("No games to save")
        
    fieldnames = [
        'Team',
        'Opponent',
        'Team_Score',
        'Opp_Score',
        'Spread',
        'Spread_Covered',
        'Final_Score',
        'Date'
    ]
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(games)

def main():
    try:
        # Specify your date range here
        start_date = '2025-02-10'
        end_date = '2025-02-12'
        
        print(f"Fetching data for dates between {start_date} and {end_date}...")
        
        dates = get_date_range(start_date, end_date)
        all_games = []
        
        for date_str in dates:
            print(f"\nFetching data for {date_str}...")
            try:
                data = fetch_odds_data(date_str)
                games = process_games(data)
                all_games.extend(games)
                print(f"Found {len(games)//2} games for {date_str}")  # Divide by 2 since we have home and away entries
            except requests.exceptions.RequestException as e:
                print(f"Error fetching data for {date_str}: {str(e)}")
                continue
        
        if all_games:
            output_file = f'/Users/PaulVallace/Desktop/College Basketball/historical data/Past Games/game_results_{start_date}_{end_date}.csv'
            save_to_csv(all_games, output_file)
            print(f"\nTotal games processed: {len(all_games)//2}")  # Divide by 2 for actual game count
            print(f"Results saved to {output_file}")
        else:
            print("No games found for the specified date range")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()