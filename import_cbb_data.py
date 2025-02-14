from web_scrape import scrape_table_to_csv
import urllib.parse

# Example usage for multiple URLs
urls = [
    "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_home_fav",  # home fav
    "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_away_dog",  # away dog
    "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=vs_ranked",    # ranked
    "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_home_dog",  # home dog
    "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_away_fav",  # away fav
    "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_home",      # home
    "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_away"       # away
]

for url in urls:
    # Extract the label from the URL query string
    parsed_url = urllib.parse.urlparse(url)
    label = urllib.parse.parse_qs(parsed_url.query).get('sc', ['default'])[0]
    
    # Set the output file name based on the label
    output_file = f"/Users/PaulVallace/Desktop/College Basketball/Tables/{label}.csv"
    
    # Scrape and save the data
    scrape_table_to_csv(url, output_file)