from fastapi import FastAPI
import random
from ddtrace import tracer
import uvicorn

app = FastAPI()

quotes = [
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]


@app.get('/')
def index():
    with tracer.trace("get_quote") as span:
        quote = random.choice(quotes) + "\n"
        span.set_tag("quote", quote)
        return quote


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5050)
