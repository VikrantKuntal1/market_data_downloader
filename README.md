
# 🥕 PrimeFresh APMC Market Data Automation

This project automates the **daily download and storage of APMC (Agricultural Produce Market Committee) market rates** for vegetables and fruits from the **Bombay market**, and automatically uploads them to a **Google Sheet** for analysis.

It eliminates manual data entry by:
- Downloading the latest market prices directly from the source website
- Saving a daily backup locally as a `.csv`
- Uploading the cleaned data into a shared **Google Sheet**, with a new tab created for each day

This automation helps the **Prime Fresh Limited** supply chain and procurement team:
- Track daily price movements  
- Analyze trends over time  
- Save hours of manual effort every morning  

---
---

## ⚙️ Features

✅ Automatically fetches live market data  
✅ Saves a daily CSV file locally (`/data/market_data_YYYY-MM-DD.csv`)  
✅ Uploads to Google Sheets using a secure **service account**  
✅ Creates a new sheet tab for each day  
✅ Can be scheduled to run automatically (macOS cron or cloud)  
✅ Simple for non-technical users — no Python knowledge required  

---

## 🧱 Folder Structure
```
market_data_downloader/
│
├── download_data.py                     # Main automation script
├── requirements.txt                      # Python dependencies
├── .gitignore                            # Prevents credentials & temp files from uploading
└── README.md                             # Documentation
```
---

## ⚙️ Setup & Installation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/VikrantKuntal1/market_data_downloader.git
cd market_data_downloader

```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add your Google credentials (⚠️ do not commit to GitHub)
  1.	Download your Service Account JSON file from Google Cloud.
	2.	Save it in this folder — for example:
```bash
primefresh-marketdata-3a7ea16c7ddf.json
```
	3.	Open your target Google Sheet and share it with the service account email inside that JSON file
(under "client_email" → give Editor access).

### 4️⃣ Enable APIs (only once)

Enable these for your Google Cloud project:
	•	Google Sheets API
	•	Google Drive API

### ▶️ Run the Script
```bash
python download_data.py
