import re

s='qwewqra'
ret=re.match(r'((qw)ewqr)a',s)
print(ret.group(2))
ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
def fun(m,*args,**kwargs):
    print(args,kwargs)
fun(1,2,3,o=3)