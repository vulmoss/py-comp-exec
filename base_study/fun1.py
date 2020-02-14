#-*-coding:utf-8-*-

def isDivisibleBy7(n,*arg):
    return type(n) == int

"""

    if type(n) == int:
        return True
    else:
        return False
"""

if __name__ == '__main__':
    print(isDivisibleBy7(20))
    print(isDivisibleBy7(20,33))
    print(isDivisibleBy7('x'))
