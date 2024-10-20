#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/10/20 17:39
# @Author   : VulMoss
# @Site     : 
# @File     : guess_sum.py
# @Software : PyCharm

import random
import hashlib
import textwrap
from mnemonic import Mnemonic


def getNumber():
    random_sum = ''.join([str(random.randint(0, 1)) for i in range(256)])
    encoded_str = random_sum.encode('utf-8')
    hash_object = hashlib.sha256()
    sum_sha256 = hash_object.update(encoded_str)
    sha_hex = hash_object.hexdigest()
    sha_bin = bin(int(sha_hex, 16))[2:]
    sha_bin8 = sha_bin[:8]
    final_sum = ''.join([random_sum, sha_bin8])
    return(final_sum)

def convertDict(array):
    dictionary = {}
    for i, value in enumerate(array):
        dictionary[value] = i
    return (dictionary)

def splitEleven(f):
    return(textwrap.wrap(f, width=11))

def convertMne(s):
    mnemo = Mnemonic("english")
    word_list = mnemo.wordlist
    dictMnemo = convertDict(word_list)
#    print(dictMnemo)
    for i in range(len(s)):
#        return 0
        print(s)

def convertBintoTen(s):
    num_from_bin = int(s, 2)
    return num_from_bin

if __name__ == '__main__':
    m = splitEleven(getNumber())
    convertMne(m)