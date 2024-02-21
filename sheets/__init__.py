import datetime
from pprint import pprint
import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

# File CREDENTIALS in Google Developer Console
CREDENTIALS_FILE = 'expenses-calc-391417-3717f41c645c.json'
# ID Google Sheets
spreadsheet_id = '1V3Xb8Rps3JsVqouIjAKwFxzcUTYxeYxAzi72gxEqxJU'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


# read file
def start_read():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:E10',
        majorDimension='COLUMNS'
    ).execute()
    pprint(values)


# write to file
def start_write():
    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "B3:C4",
                 "majorDimension": "ROWS",
                 "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
                {"range": "D5:E6",
                 "majorDimension": "COLUMNS",
                 "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
            ]
        }
    ).execute()


def write_new_row(message):
    row = message.text
    message_time = message.date
    message_time = datetime.datetime.utcfromtimestamp(message_time)
    today = message_time.strftime('%Y-%m-%d %H:%M:%S')
    #today = date.today()
    values = [[row, today]]
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="A1",
        valueInputOption='RAW',
        body=body).execute()
