# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Carlin"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
