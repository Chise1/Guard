# -*- encoding: utf-8 -*-
"""
@File    : serializers.py
@Time    : 2020/3/28 17:24
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from typing import Optional

from pydantic import BaseModel
from fastapi import APIRouter, Depends

from main import oauth2_scheme

user_router=APIRouter()
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@user_router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

