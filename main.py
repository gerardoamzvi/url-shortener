from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import string
import random

urls : dict[str, str] = {}
class URLRequest(BaseModel):
    url: str

def generate_short_code(length: int = 6) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_unique_short_code(max_attempts: int = 10) -> str:
    for i in range(max_attempts):
        short_code = generate_short_code()
        if short_code not in urls:
            return short_code
    raise HTTPException(status_code=500, detail="Failed to generate a unique short code")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}

@app.post("/shorten")
def shorten_url(url_request: URLRequest):
    if not url_request.url.startswith("http://", "https://"):
        raise HTTPException(status_code=400, detail="Invalid URL")
    short_code = generate_unique_short_code()
    urls[short_code] = url_request.url
    return {"short_code": short_code}

@app.get("/{code}")
def redirect_to_url(code: str):
    if short_code not in urls:
        raise HTTPException(status_code=404, detail="Short code not found")
    return RedirectResponse(urls[short_code])


