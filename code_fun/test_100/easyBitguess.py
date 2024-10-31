#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/10/31 22:16
# @Author   : VulMoss
# @Site     : 
# @File     : easyBitguess.py
# @Software : PyCharm


import bitcoin
import random
import hashlib
import textwrap
from mnemonic import Mnemonic
# 生成私钥
###private_key = bitcoin.random_key()

# 根据私钥生成公钥
###public_key = bitcoin.privtopub(private_key)

# 根据公钥生成比特币地址
###bitcoin_address = bitcoin.pubtoaddr(public_key)

###print("Private key:", private_key)
####print("Public key:", public_key)
####print("Bitcoin address:", bitcoin_address)

private_bit = bin(int(private_key, 16))[2:]
print("pri2:",private_bit)



def convertDict(array):
    dictionary = {}
    for i, value in enumerate(array):
        dictionary[value] = i
    return (dictionary)

def splitEleven(private_bit):
    return(textwrap.wrap(private_bit, width=11))

def convertMne(s):
    mnemo = Mnemonic("english")
    word_list = mnemo.wordlist
    dictMnemo = convertDict(word_list)
    matching_keys = [key for value in s for key,val in dictMnemo.items() if val == value]
    print(' '.join(map(str,matching_keys)))


def convertBintoTen(str_list):
    num_list = [int(item,2) for item in str_list]
    return ( num_list)

if __name__ == '__main__':
    private_key = bitcoin.random_key()
    private_bit = bin(int(private_key, 16))[2:]
    s = convertBintoTen(private_bit)
    convertMne(s)