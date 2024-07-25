from fastapi import FastAPI
import custom_math

app = FastAPI()

@app.get("/")
async def root():

    return {"message": "Hello World"}



@app.get("/add")
async def add_numbers(a: int = 1, b: int = 1):

    result = custom_math.add(a, b)

    return {"result": result}
