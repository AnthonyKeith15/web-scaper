# Web Scraping with Selenium and BeautifulSoup

This script allows you to scrape data from web pages using Selenium and BeautifulSoup. It uses Selenium to automate the browser interaction and BeautifulSoup to parse the HTML content.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- Selenium (`pip install selenium`)
- BeautifulSoup (`pip install beautifulsoup4`)

You will also need to download the appropriate ChromeDriver executable for your operating system and place it in the script's directory. You can download the ChromeDriver from the official website: [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/)

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script is located.

2. Run the script using the following command: (`python3 main.py`)

3. You will be prompted to enter the URL of the website you want to scrape. Provide the URL and press Enter.

4. You will then be prompted to enter the name of the JSON file where you want to save the scraped data. Enter the file name (e.g., `data.json`) and press Enter.

5. The script will open a Chrome browser window controlled by Selenium. Once the page has loaded, you will be prompted to press any key to start scraping or 'q' to quit.

6. When prompted, press any key to start scraping. The script will extract table data from the webpage and save it to the specified JSON file.

7. If there are multiple tables on the webpage, the script will scrape each table and append the data to the existing JSON file.

8. After scraping, you will have the option to press 'q' to quit or any other key to scrape another page. If you choose to scrape another page, repeat steps 3-7.

9. Once you're done scraping, you can find the JSON file with the scraped data in the same directory as the script.

## Notes

- Make sure you have a stable internet connection for the script to load web pages and scrape data properly.

- The script assumes that the table structure on the web page follows the standard HTML table format. If the table structure is different, you may need to modify the script accordingly.

- If you encounter any issues or errors, try updating the Selenium and BeautifulSoup libraries to their latest versions.

- This script is for educational and personal use only. Make sure to respect the website's terms of service and avoid scraping sensitive or private data without proper permission.
