# -*- encoding: utf-8 -*-
"""
@File    : middlewares.py
@Time    : 2020/3/28 16:49
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :全局中间件
"""
from fastapi import Request
import hashlib
import hmac
from fastapi import HTTPException
from app.server.serializers import HeartbeatSerializer, TokenSerializer

from settings import SECRET



async def add_process_time_header(request: Request, call_next):
    """增加处理时间"""
    print(request)
    if request.method=="POST" or request.method=="PUT" or request.method=="DELETE" :
        print("1")
        pass
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(0)
    return response