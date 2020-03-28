# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2020/3/28 15:00
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
import uvicorn
from fastapi import FastAPI, Depends
from middlewares import add_process_time_header
from fastapi.security import OAuth2PasswordBearer
app=FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app.middleware('http')(add_process_time_header)

@app.get("/items/")
async  def read_items(token:str=Depends(oauth2_scheme)):
    return {"token":token}
@app.get('/')
def root():
    return {"msg":"Hello Guard"}
from app.server.server import router
app.include_router(router,tags=['heartbeat'],)

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
