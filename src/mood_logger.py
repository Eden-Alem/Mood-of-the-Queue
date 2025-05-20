import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "creds.json"
SHEET_NAME = "MoodQueue"

def get_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet


def log_mood(sheet, mood: str, note: str = ""):
    timestamp = datetime.now().isoformat()
    sheet.append_row([timestamp, mood, note])


def get_all_moods(sheet):
    return sheet.get_all_records()
