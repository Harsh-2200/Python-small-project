import dis

def test(number):
    return (str(number)+str(number))

def newFunc(string):
    print('hello',string)

dis.dis(test)

dis.dis(newFunc)
