from scraper import *
from spreadsheet import *
from config import VIEW_IDS



analytics = createAnalyticsReport()

start_date = input("Start Date? (yyyy-mm-dd)\n")
end_date = input("End Date? (yyyy-mm-dd)\n")

worksheet = makeNewMonth(start_date)
append_title(worksheet)
for url,id in VIEW_IDS.items():
    row = getResponse(analytics, start_date, end_date, id)
    row.insert(0,url)
    append_row(row, worksheet)
