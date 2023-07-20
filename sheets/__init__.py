from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import datetime, time

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'expenses-calc-391417-3717f41c645c.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1QBONjulgacOEFTAGcTW69UQ1l0iOhaQQTVcpdPwfTEU'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


# Пример чтения файла
def start_read():
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:E10',
        majorDimension='COLUMNS'
    ).execute()
    pprint(values)


# Пример записи в файл
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
    messageTime = message.date
    messageTime = datetime.datetime.utcfromtimestamp(messageTime)
    today = messageTime.strftime('%Y-%m-%d %H:%M:%S')
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
