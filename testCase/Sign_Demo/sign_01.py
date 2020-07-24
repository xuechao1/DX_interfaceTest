# -*- coding:utf-8 -*-

'''
sign签名主要是用于提供给外部(第三方)调用的接口,需要提供appkey钥匙才能调用
'''
import hashlib

appkey = "111222333"
body = {
    "username": "Test",
    "Password": "123456",
    "mail": "",
    "sign": "xxx"
}
# todo 第1步： 将所有参数(注意是所有参数)，除去sign本身，以及值是空的参数，转化为键值对的

# s = ["".join(i) for i in body.items() if i[1] != "" and i[0] != "sign"]
# print(s)

list = []
for i in body.items():
    if i[1] != "" and i[0] != "sign":
        list.append("".join(i))
print(list)

# todo 2：排序后的参数按照参数1值1，参数2值2的键值对顺序拼接成一个字符串，按参数名字母升序排序
# TODO 按字母升序排序
sort = "".join(sorted(list))
print(sort)

# todo 3:在第二步得到的字符串后面，加上接入方验证密匙key，然后计算md5值，
result = sort + appkey
print(result)


# todo MD5加密,固定的写法
def jiami(params):
    m = hashlib.md5()
    m.update(params.encode("utf-8"))
    return m.hexdigest()


sign = jiami(result.lower())  # lower()把字符转为小写
print(sign)
