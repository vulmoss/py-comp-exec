#!/usr/bin/env python3

import csv
with open('./test/test.csv') as f:
    data = csv.reader(f)
    list1 = list(data)

for i in list1:
    print(i)


