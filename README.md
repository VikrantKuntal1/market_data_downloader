# market_data_downloader
Automated script to download and store daily market data for Prime Fresh Limited, enabling data-driven price analysis and strategic decisions.
# 📊 Market Data Downloader

This project automates the **daily download and storage of market data** used by **Prime Fresh Limited** for price analysis, forecasting, and strategic decision-making.

---

## 🚀 Features

- 🔁 Automatically fetches the latest market data (from Moneycontrol or other sources)
- 📅 Saves data as CSV files with date-based filenames (e.g., `market_data_2025-11-03.csv`)
- 🧾 Logs every run (success or error)
- ☁️ Can be hosted on **Render.com** for daily automation
- 🌐 Includes a `/run` web endpoint to trigger manual data download anytime

---

## 🗂️ Folder Structure
```
market_data_downloader/
│
├── app.py                  # FastAPI web app (provides /run endpoint)
├── download_data.py        # Core script that downloads and saves market data
├── requirements.txt        # Python dependencies
├── data/                   # Folder where CSV files are stored
└── download_log.txt        # Auto-created log of download history
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

### 3️⃣ Run locally
```bash
python download_data.py
