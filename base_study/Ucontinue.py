#-*-coding:utf-8-*-

i = 0
while True:
    i += 1
    print('i1 is %d',i)
    if i == 10:
        print('Iam 10')
        continue
    print('i2 is %d',i)
    if i == 20:
        break

