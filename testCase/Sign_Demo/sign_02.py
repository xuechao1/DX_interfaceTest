# -*- coding:utf-8 -*-

import hashlib


def get_sign(body, appkey="111222333"):
    list = []
    for i in body.items():
        if i[1] != "" and i[0] != "sign":
            list.append("".join(i))
    sort = "".join(sorted(list))
    result = sort + appkey
    return result.lower()


def jiami(params):
    m = hashlib.md5()
    m.update(params.encode("utf-8"))
    return m.hexdigest()


body = {
    "username": "Test",
    "Password": "123456",
    "mail": "",
    "sign": "xxx"
}
# print(body.get("sign"))  # todo get取字典的值不会报异常
# print(body["username"])
sign = jiami(get_sign(body))  # lower()把字符转为小写
print(sign)
