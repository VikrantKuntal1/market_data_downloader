# app.py
from fastapi import FastAPI
from download_data import run_downloader

app = FastAPI()

@app.get("/")
def home():
    return {"status": "✅ Market data downloader is live"}

@app.get("/run")
def run_download():
    run_downloader()
    return {"message": "Data download triggered successfully!"}