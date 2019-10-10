# Google Analytics Monthly Scraper

This is a Python command line tool to scrape google analytics data into a google sheets document built with Google Analytics API and Google Sheets API.

## Setup
Fill in missing information in `client_secrets.json`, `config.py`, and `scraper.py`.

## Dependencies
install these dependencies

`pip install httplib2 oauth2client google-api-python-client google datetime gspread`


## Usage

In the root directory run this tool with
`python main.py`


## Adding New Websites
Add url and view id of new site in `config.py`

## Adding New metrics
You will need to modify the list of metrics in scraper.getResponse and list of row titles in spreadsheet.append_title

## Other Notes
With this tool you can't create 2 reports in the same month and year (ex: March 2019) , if you receive an error while creating a new sheet it is probably because theres already a sheet for that month and year
