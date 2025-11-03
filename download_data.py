import requests
import pandas as pd
import os
from datetime import datetime
from io import StringIO



# ✅ Replace with your actual market data URL
url = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"   # example placeholder

# ✅ Folder to store CSV files
folder = "data"
os.makedirs(folder, exist_ok=True)

try:
    # Step 1: Fetch data
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()  # raise an error if download fails

    # Step 2: Parse data
    try:
        # Case 1: If the site gives JSON
        data = response.json()
        df = pd.DataFrame(data)
    except ValueError:
        # Case 2: If it’s HTML (try to read table)
        df = pd.read_html(StringIO(response.text))[0]

    # Step 3: Save CSV with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(folder, f"market_data_{timestamp}.csv")
    df.to_csv(file_path, index=False)

    print(f"✅ Market data saved: {file_path}")

except Exception as e:
    print(f"❌ Error downloading data: {e}")