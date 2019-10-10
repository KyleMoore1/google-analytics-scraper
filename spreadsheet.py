import gspread
from oauth2client.service_account import ServiceAccountCredentials
import calendar

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    './client_secrets.json', scope)

client = gspread.authorize(creds)

spreadSheet = client.open('<your spreadsheet name here>')


def makeNewMonth(start_date):
    date = start_date.split('-')
    month_num = int(date[1])
    year = date[0]
    worksheet_title = calendar.month_name[month_num] + ' ' + year
    return spreadSheet.add_worksheet(worksheet_title, 10, 1000)


def append_row(row, worksheet):
    worksheet.append_row(row, 'USER_ENTERED')


def append_title(worksheet):
    title_row = ['Website URL', 'Users', 'New Users', 'Sessions', 'Sessions/User',
                 'Pageviews', 'Pages/Session', 'Avg Session Duration', 'Bounce Rate']
    worksheet.append_row(title_row, 'USER_ENTERED')
