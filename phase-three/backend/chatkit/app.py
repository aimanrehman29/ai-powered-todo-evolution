from fastapi import FastAPI

app = FastAPI(title="ChatKit Backend")

@app.get("/")
def root():
    return {"Hello": "World!"}
