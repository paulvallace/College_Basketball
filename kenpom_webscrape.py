from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime, timedelta
import time

def get_date_range(start_date_str: str, end_date_str: str) -> list:
    """Generate a list of dates between start and end date."""
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates

def scrape_kenpom_data(driver, date):
    """Scrape data for a specific date."""
    url = f"https://kenpom.com/archive.php?d={date}"
    driver.get(url)
    time.sleep(3)  # Wait for data to load
    
    # Find all rows using XPath
    rows = driver.find_elements(By.XPATH, "//table[@id='ratings-table']//tr")
    
    data = []
    for row in rows[1:]:  # Skip header row
        try:
            # Extract all required columns
            cells = row.find_elements(By.XPATH, ".//td")
            if len(cells) >= 9:  # Ensure we have enough cells
                row_data = [
                    cells[0].text,  # Rk
                    cells[1].text,  # Team
                    cells[2].text,  # Conf
                    cells[3].text,  # NetRtg
                    cells[4].text,  # ORtg
                    cells[5].text,  # DRtg
                    cells[6].text,  # AdjT
                    cells[7].text,  # Rk (second)
                    cells[8].text   # NetRtg (second)
                ]
                row_data.append(date)  # Add date column
                data.append(row_data)
                
        except Exception as e:
            print(f"Error processing row for date {date}: {str(e)}")
            continue
            
    return data

def login_to_kenpom():
    chrome_options = webdriver.ChromeOptions()
    all_data = []
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=chrome_options)
        
        # Login process
        driver.get("https://kenpom.com/")
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'][name='email'][placeholder='E-mail']"))
        )
        password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password'][name='password'][placeholder='Password']")
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='submit'][value='Login!']")
        
        email_field.send_keys("tgaston@wisc.edu")
        password_field.send_keys("Jakel123")
        submit_button.click()
        time.sleep(2)
        
        # Define date range
        start_date = '2025-02-11'  # Adjust these dates as needed
        end_date = '2025-02-13'
        dates = get_date_range(start_date, end_date)
        
        # Scrape data for each date
        for date in dates:
            print(f"Scraping data for {date}")
            data = scrape_kenpom_data(driver, date)
            all_data.extend(data)
            time.sleep(1)  # Prevent too many rapid requests
        
        # Create DataFrame
        columns = ['Rk', 'Team', 'Conf', 'NetRtg', 'ORtg', 'DRtg', 'AdjT', 'Rk2', 'NetRtg2', 'Date']
        df = pd.DataFrame(all_data, columns=columns)
        
        # Clean numerical columns
        numeric_cols = ['Rk', 'NetRtg', 'ORtg', 'DRtg', 'AdjT', 'Rk2', 'NetRtg2']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col].str.replace('+', ''), errors='coerce')
        
        # Save to Excel
        output_file = f'/Users/PaulVallace/Desktop/College Basketball/historical data/Kenpom/kenpom_{start_date}_{end_date}.xlsx'
        df.to_excel(output_file, index=False, engine='openpyxl')
        
        print(f"\nData saved to {output_file}")
        print("\nFirst few rows of data:")
        print(df.head())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Current URL:", driver.current_url)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    login_to_kenpom()
