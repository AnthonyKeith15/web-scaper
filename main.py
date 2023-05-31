from selenium import webdriver
from bs4 import BeautifulSoup
import os
import json

# Get the path to the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the ChromeDriver executable
chrome_driver_path = os.path.join(current_directory, "..", "chromedriver_mac64", "chromedriver")

# Configure Selenium webdriver
driver = webdriver.Chrome(chrome_driver_path)

# Prompt the user for the URL of the website
url = input("Please enter the URL of the website you want to scrape: ")

# Prompt the user for the name of the JSON file
json_file_name = input("Please enter the name of the JSON file you want to save the data to (e.g. 'data.json'): ")
json_file_path = os.path.join(current_directory, json_file_name)

# Load the webpage using Selenium
driver.get(url)

# Check if the specified JSON file already exists
player_data = []

if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as json_file:
        player_data = json.load(json_file)


while True:
    # Use input() to pause the program until you're ready to start scraping
    input("Press any key to start scraping or 'q' to quit...")

    # Get the page source after it has loaded
    page_source = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Find all table elements on the webpage
    tables = soup.find_all("table")

    if tables:
        for table in tables:
            # Extract the table headers
            headers = [th.text.strip() for th in table.find_all("th")]

            # Extract the table rows
            rows = []
            for tr in table.find_all("tr"):
                row = []
                for td in tr.find_all("td"):
                    first_child = td.find()
                    if first_child and first_child.name == "img":
                     row.append("image")
                    else:
                        row.append(td.text.strip())
                if row:
                    rows.append(row)

            # Convert each row to a dictionary with headers as keys
            table_data = [dict(zip(headers, row)) for row in rows]

            # Append table data to the existing player_data
            player_data.extend(table_data)

            # Write updated player data to the JSON file
            with open(json_file_path, 'w') as json_file:
                json.dump(player_data, json_file)

            print("Player data appended to", json_file_name)

            print("\n---\n")  # Print a separator between tables
    else:
        print("No tables found on the webpage.")

    # Check if user wants to quit
    if input("Press 'q' to quit or any other key to scrape another page: ") == 'q':
        break

# Close the Selenium webdriver
driver.quit()

