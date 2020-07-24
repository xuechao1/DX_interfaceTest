# -*- coding:utf-8 -*-

import requests
from pprint import pprint

host = "http://3.85.16.233:32100"
# url = host+'/User/getMyFollow'
url = host+'/User/getMyFollow?timezone=Asia%2FShanghai' \
           '&userKeyWithoutImei=4e701c7505ce494c7b28be2da07b6f3b&channel=dreameoppo-46' \
           '&advertising_id=4cd19094-1fdd-436a-8f65-d7f3c27f536f' \
           '&sign=2d19e9c35083383302b1c8ed48eb79d9&mcc=460&versionName=1.7.4' \
           '&deviceId=b1364ddb106b056c&uuid=9f223804-130d-4069-8f94-b9739a85c813' \
           '&userKey=b1232786105b6a3c82c0fa447d3946f4&versionCode=125' \
           '&s=eyJrIjoiZDIzOWNjOWI3ZTc5ZTBkNDI1NTQwMTFjYjM4MjgxNDkiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIs' \
           'ImEiOjEsIkwiOjE2LCJsIjoxNTkxNzY5NzUzLCJyIjowLCJzIjoiZDVhNGIxNTUxZDI2NjI4ZDNhNWExMTV' \
           'hOWViYThlNjYifQ%3D%3D&u=eyJxIjo0Mjk2MDAwMzI1LCJNIjoiclVJeUwydXVvbEgwWlVBMExLVzVZemsw' \
           'TU49PSIsIm4iOiJraHJwdW5iIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTc2MDgxOCwiYyI6MCwiYiI6IiIsI' \
           'mUiOiJ4dWVjaGFvQHN0YXJ5Lmx0ZCIsImlzQXV0aG9yIjpmYWxzZX0%3D&distinct_id=b1364ddb106b056c' \
           '&osType=0&imei=866716038443093&appKey=201020412&interfaceCode=122&apiLevel=28' \
           '&androidId=b1364ddb106b056c'
data = {
    "timezone":"Asia%2FShanghai",
    "userKeyWithoutImei":"4e701c7505ce494c7b28be2da07b6f3b",
    "channel":"dreameoppo-46",
    "advertising_id":"4cd19094-1fdd-436a-8f65-d7f3c27f536f",
    "sign":"2d19e9c35083383302b1c8ed48eb79d9",
    "mcc":"460",
    "versionName":"1.7.4",
    "deviceId":"b1364ddb106b056c",
    "uuid":"9f223804-130d-4069-8f94-b9739a85c813",
    "userKey":"b1232786105b6a3c82c0fa447d3946f4",
    "versionCode":"125",
    "s":"eyJrIjoiZDIzOWNjOWI3ZTc5ZTBkNDI1NTQwMTFjYjM4MjgxNDkiLCJTIjoiamluZ3l1IiwidiI6IjEuMCIsImEiOjEsIkwiOjE2LCJsIjoxNTkxNzY5NzUzLCJyIjowLCJzIjoiZDVhNGIxNTUxZDI2NjI4ZDNhNWExMTVhOWViYThlNjYifQ%3D%3D",
    "u":"eyJxIjo0Mjk2MDAwMzI1LCJNIjoiclVJeUwydXVvbEgwWlVBMExLVzVZemswTU49PSIsIm4iOiJraHJwdW5iIiwiaSI6IiIsInMiOiIwIiwibSI6MTU5MTc2MDgxOCwiYyI6MCwiYiI6IiIsImUiOiJ4dWVjaGFvQHN0YXJ5Lmx0ZCIsImlzQXV0aG9yIjpmYWxzZX0%3D",
    "distinct_id":"b1364ddb106b056c",
    "osType":"0",
    "imei":"866716038443093",
    "interfaceCode":"122",
    "apiLevel": "28",
    # "debug": "panjian",
    "androidId": "b1364ddb106b056c"
}
# res = requests.post(url=url,data=data)
res = requests.get(url)
pprint(res.json())
