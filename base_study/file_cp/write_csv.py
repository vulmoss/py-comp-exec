#!/usr/bin/env python3

import csv
with open('./test/test.csv') as f:
    data = csv.reader(f)
    list1 = list(data)

with open('./test/test2.csv','w') as f1:
    csv.writer(f1).writerow(list1)

