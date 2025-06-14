# OBD Fault Code Scraper

A Python script that scrapes OBD-II fault codes from [revue-technique-auto.fr](https://www.revue-technique-auto.fr/codes-defauts-obd) and exports them to a CSV file.

## Features

- Scrapes fault codes for multiple car brands
- Handles pagination automatically
- Outputs clean CSV data with brand, category, code, and description
- Easy to use with no database required

## How to Use

1. Install requirements:
   ```bash
   pip install requests beautifulsoup4
2. Run the script:
   ```bash
   python obd_scraper.py
- Wait for scraping to complete (may take several minutes)
- Find your data in obd_codes.csv
3. Supported Brands:
 -   Audi
 -   BMW
 -   Citroën
 -   Dacia
 -   Fiat
 -   Ford (EU)
 -   Mercedes
 -   Opel
 -   Peugeot
 -   Renault
 -   (and more)
4. Disclaimer:
This project is for educational purposes only. Please respect the website's terms of service and robots.txt. Use responsibly and consider adding delays between requests.
