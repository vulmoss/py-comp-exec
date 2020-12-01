#!/usr/bin/env python3

filename = input('plwase input the name: ')
with open(filename) as file:
    count = 0
    for line in file:
        count += 1
        print(line)
    print('lines :',count)

