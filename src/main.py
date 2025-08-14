import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()



app = FastAPI()


class Operation(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    env = os.getenv("ENV", "Not_Defined")
    return {"message": "Welcome to the FastAPI app!", "env": env}


@app.post("/add")
def add_numbers(op: Operation):
    return {"result": op.a + op.b}

@app.post("/subtract")
def subtract_numbers(op: Operation):
    return {"result": op.a - op.b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0", port=8000)



