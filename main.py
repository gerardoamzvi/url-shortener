from fastapi import FastAPI
from pydantic import BaseModel
import string
import random

class URLRequest(BaseModel):
    url: str

def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


app = FastAPI()


@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}


