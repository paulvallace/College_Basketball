import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_table_to_csv(url, output_file):
    """
    Scrapes table data from a given URL and saves it to a CSV file.

    Args:
        url (str): The URL of the webpage to scrape.
        output_file (str): The name of the output CSV file.

    Returns:
        None
    """
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table with the required data
        table = soup.find('table', class_='tr-table')  # Adjust the class name if necessary
        if not table:
            print(f"No table found on {url}")
            return

        # Extract table headers
        headers = [header.text.strip() for header in table.find('thead').find_all('th')]

        # Extract table rows
        rows = []
        for row in table.find('tbody').find_all('tr'):
            cols = [col.text.strip() for col in row.find_all('td')]
            rows.append(cols)

        # Convert the data into a pandas DataFrame
        data = pd.DataFrame(rows, columns=headers)

        # Rename columns to match the desired format
        data.rename(columns={
            'Team': 'Team',
            'ATS Record': 'ATS Record',
            'Cover %': 'Cover %',
            'MOV': 'MOV',
            'ATS +/-': 'ATS +/-'
        }, inplace=True)

        # Save the DataFrame to a CSV file
        data.to_csv(output_file, index=False)
        print(f"Data successfully scraped and saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while scraping {url}: {e}")

# Example usage for multiple URLs
# urls = [
#     "https://www.teamrankings.com/ncb/trends/ats_trends/",
# ]

# for i, url in enumerate(urls, start=1):
#     output_file = f"output_data_{i}.csv"
#     scrape_table_to_csv(url, output_file)
