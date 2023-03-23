# https://github.com/Sanjeev-Thiyagarajan/fastapi-course/tree/main/app


from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Learning Management System"}
