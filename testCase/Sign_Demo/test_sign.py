# -*- coding:utf-8 -*-


import datetime
import hashlib


today = str(datetime.date.today()).split('-')
a = ''.join(today)
d = a+'but4NC5RWATYr30DuVf0ylAZL571oBGH'
d1 = hashlib.md5()
d1.update(d.encode('utf-8'))
f = d1.hexdigest()
print(f)
sign = '49120408eabadff48af0cca149225759'

