# -*- encoding: utf-8 -*-
"""
@File    : server.py
@Time    : 2020/3/28 15:07
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :哨兵服务器接收信息并返回基本信息
"""
from fastapi import APIRouter, Depends, Header, Body
from pydantic import BaseModel
from dependencies import token_is_true


router=APIRouter()
class Test(BaseModel):
    info:str
@router.post("/heartbeat")
def heartbeat(msg:str=Header(...,description="测试msg"),test:Test=Body(...,),token:dict=Depends(token_is_true)):
    return {"code":0,"msg":"success","test":test}
