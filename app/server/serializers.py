# -*- encoding: utf-8 -*-
"""
@File    : serializers.py
@Time    : 2020/3/28 15:09
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from fastapi import Body, Header
from pydantic import BaseModel, Field


class TokenSerializer(BaseModel):
    server_id: str=Header(...,)
    nonce: str=Header(...,)
    timestamp: str=Header(...,)
    token:str= Header(..., description="token验证")


class HeartbeatSerializer(BaseModel):
    info: str = Field(..., max_length=128, description="服务器上传xinxi")


class HeartbeatResSerializer(BaseModel):
    code: int = Field(0, description="默认为0，如果非正常则为非0")
    msg: str = Field("success", description="返回的信息，如果报错会返回错误信息")
