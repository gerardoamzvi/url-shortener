# URL Shortener — CI/CD with GitHub Actions

A minimal FastAPI service that shortens URLs and redirects to the original address. Built to practice continuous integration (CI) with GitHub Actions.

## Endpoints

- `POST /shorten` — submit a URL and receive a short code
- `GET /{code}` — redirect to the original URL

## Running the project

```bash
uv run uvicorn main:app --reload
```

The API will then be available at `http://127.0.0.1:8000`, with interactive documentation at `http://127.0.0.1:8000/docs`.


## Running tests locally 

```bash
uv run pytest -v 
```