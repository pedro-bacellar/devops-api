from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/soma")
def soma(a: int, b: int):
    return {"resultado": a + b}