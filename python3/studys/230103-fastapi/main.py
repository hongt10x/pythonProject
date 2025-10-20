# coding=utf-8
# time: 2023/12/19 17:24
# file: study_231219.py
# author: wht


from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}

if __name__ == '__main__':
    uvicorn.run(app="main:app",host="127.0.0.1",port=8008,reload=True)



