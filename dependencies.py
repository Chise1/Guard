# -*- encoding: utf-8 -*-
"""
@File    : Dependencies.py
@Time    : 2020/3/28 15:37
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :全局依赖
"""
import hashlib
import hmac
from fastapi import HTTPException, Header
from settings import SECRET


def get_sign(ak: str, nonce: str, ts: str, sk: str):
    """生成签名"""
    # self.nonce = str(uuid.uuid1()).replace("-", "")
    # nonce = str(uuid.uuid1()).replace("-", "")
    a = [ak, nonce, ts]
    a.sort()
    # a = [self.ak, 'ZPMxNpPhmrPzQj27AGKijM3FmEcHW4BY', '1550032562']

    join_str = "".join(a)
    # print(join_str)
    return hmac.new(sk.encode(), join_str.encode(), hashlib.sha256).hexdigest()


import time


async def token_is_true(server_id: str = Header(..., ), nonce: str = Header(..., ), timestamp: str = Header(..., ),
                        token: str = Header(..., description="token验证")):
    """签名验证，全局使用,超过60秒或者验证失败就会报错"""
    if time.time() - int(timestamp) > 60 or token == get_sign(server_id, nonce, timestamp, SECRET):
        raise HTTPException(
            status_code=401,
            detail="token is fail",
            headers={"X-Error": "There goes my error"},
        )
    else:
        return {"server_id": server_id}
