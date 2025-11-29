from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

dani = {"temp": 0, "hum": 0}

@app.post("/data")
async def otrymano(info: dict):
    global dani
    dani = info
    print("Отримано з ESP32:", info)
    return {"status": "ok"}

@app.get("/data")
def vidprav():
    return dani

@app.get("/")
def home():
    return {"message": "ESP32 живий! Перейдіть на /docs для Swagger або відкрийте статичний сайт"}
