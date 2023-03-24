# https://github.com/Sanjeev-Thiyagarajan/fastapi-course/tree/main/app


from typing import Union
from fastapi import FastAPI
from .Features.Auth import registration



app = FastAPI()


app.include_router(registration.router)

@app.get("/")
def read_root():
    return {"message": "Learning Management System"}

