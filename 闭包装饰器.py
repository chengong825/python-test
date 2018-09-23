def addHeader(fun):
    def wrapped():
        return 'a'+fun()+'a'
    return wrapped

def addHeader2(fun):
    def wrapped():
        return 'b'+fun()+'b'
    return wrapped

@addHeader
@addHeader2
def p():
    return 'lalala'
print(p())