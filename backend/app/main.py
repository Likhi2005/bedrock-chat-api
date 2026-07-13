from fastapi import FastAPI
from simpleText.backend.app.routes import chat


app = FastAPI(
    title="AWS Bedrock Chat API",
    version="1.0"
)

app.include_router(
    chat.router
)

@app.get("/")
def root():
    return {"message": "Welcome to the AWS Bedrock Chat API!"}