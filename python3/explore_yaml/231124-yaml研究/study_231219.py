# coding=utf-8
# time: 2023/12/19 17:24
# file: study_231219.py
# author: wht


from fastapi import FastAPI
import uvicorn
import os
app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}

if __name__ == '__main__':
    uvicorn.run(app=f"{__file__.split(f'{os.sep}')[-1].split('.')[0]}:app",host="127.0.0.1",port=8008,reload=True)