#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/10/31 12:20
# @Author   : VulMoss
# @Site     : 
# @File     : test_finalSum.py
# @Software : PyCharm

import random
import hashlib
import textwrap

def getNumber():
    random_sum = ''.join([str(random.randint(0, 1)) for i in range(256)])
    encoded_str = random_sum.encode('utf-8')
    hash_object = hashlib.sha256()
    sum_sha256 = hash_object.update(encoded_str)
    sha_hex = hash_object.hexdigest()
    sha_bin = bin(int(sha_hex, 16))[0:]
    sha_bin8 = sha_bin[:8]
    final_sum = ''.join([random_sum, sha_bin8])
    print(final_sum)

if __name__ == '__main__':
     getNumber()