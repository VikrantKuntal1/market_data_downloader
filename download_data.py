import requests
import pandas as pd
import os
import random
from datetime import datetime
from io import StringIO
import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import traceback

# ==========================================================
# ✅ CONFIGURATION
# ==========================================================
URL = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
DATA_FOLDER = "data"
os.makedirs(DATA_FOLDER, exist_ok=True)

# Your Service Account JSON file (downloaded from Google Cloud)
SERVICE_ACCOUNT_FILE = "primefresh-marketdata-3a7ea16c7ddf.json"

# Your Google Sheet ID (the master sheet)
SPREADSHEET_ID = "1EVtak7Fje98-_O6kFcEcYn0EQL0FE7PAxdY-nmI9lyM"

# ==========================================================
# ✅ PREPARATION
# ==========================================================
timestamp = datetime.now().strftime("%Y-%m-%d")
file_path = os.path.join(DATA_FOLDER, f"market_data_{timestamp}.csv")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]
headers = {"User-Agent": random.choice(user_agents)}

# ==========================================================
# ✅ STEP 1: FETCH MARKET DATA
# ==========================================================
try:
    print("🔍 Fetching market data...")
    response = requests.get(URL, headers=headers, timeout=15)
    response.raise_for_status()

    try:
        data = response.json()
        df = pd.DataFrame(data)
    except ValueError:
        df = pd.read_html(StringIO(response.text))[0]

    df.to_csv(file_path, index=False)
    print(f"✅ Market data saved locally: {file_path}")

except Exception as e:
    print(f"❌ Error fetching data: {e}")
    exit()

# ==========================================================
# ✅ STEP 2: UPLOAD TO GOOGLE SHEETS (MASTER SHEET)
# ==========================================================
try:
    print("🚀 Uploading to Google Sheets (master sheet)...")

    # Define Google API scopes
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    # Authenticate with Service Account
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
    client = gspread.authorize(creds)

    # Open your master sheet
    spreadsheet = client.open_by_key(SPREADSHEET_ID)

    # Create or overwrite today's tab
    sheet_title = timestamp
    try:
        worksheet = spreadsheet.add_worksheet(title=sheet_title, rows="1000", cols="20")
        print(f"🆕 Created new sheet tab: {sheet_title}")
    except gspread.exceptions.APIError:
        worksheet = spreadsheet.worksheet(sheet_title)
        worksheet.clear()
        print(f"♻️ Overwriting existing tab: {sheet_title}")

    # Write the DataFrame to the worksheet
    set_with_dataframe(worksheet, df)

    print(f"✅ Data uploaded successfully to tab: {sheet_title}")
    print(f"📎 URL: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}")

except Exception as e:
    print("❌ Error uploading to Google Sheets:")
    traceback.print_exc()