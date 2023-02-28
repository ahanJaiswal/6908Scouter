import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)
sheet = client.open("6908_Infuzed_Scout_Data").sheet1

def newTeam(row, teamNum, teamName):
    sheet.update_cell(row, 1, teamNum)
    sheet.update_cell(row, 2, teamName)