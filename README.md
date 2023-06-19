# Cricinfo Web Scraping with Selenium

This repository contains code that utilizes Selenium and ChromeDriver to scrape text data of short blogs with their headings from the Cricinfo website. It provides a simple and efficient way to extract specific information from Cricinfo and store it in a structured format.

## Requirements

To run this code, you will need the following:

- [Selenium](https://www.selenium.dev/)
- [ChromeDriver](https://chromedriver.chromium.org/)
- [Pandas](https://pandas.pydata.org/)

## Installation

1. Install Selenium using the following command:
   ```
   pip install selenium
   ```

2. Download the appropriate version of ChromeDriver for your system and place it in the project directory. Make sure the ChromeDriver version is compatible with your installed Chrome browser.

3. Install Pandas using the following command:
   ```
   pip install pandas
   ```

## Usage

1. Clone or download this repository to your local machine.

2. Update the `PATH` variable in the code with the path to your ChromeDriver executable.

3. Run the script `cricinfo.py` to initiate the web scraping process.

4. The extracted data will be saved as a CSV file named `cricinfo.csv` in the project directory.


## Acknowledgments

Special thanks to the developers of Selenium, ChromeDriver, and Pandas for their invaluable contributions.

Happy web scraping!
