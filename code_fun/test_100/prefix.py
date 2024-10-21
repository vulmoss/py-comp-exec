#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/10/21 17:53
# @Author   : VulMoss
# @Site     : 
# @File     : prefix.py
# @Software : PyCharm


def prefix_to_subnet_mask(prefix_length):
    binary_mask = ''.join(['1'] * prefix_length) + ''.join(['0'] * (32 - prefix_length))
    binary_mask = [binary_mask[i:i + 8] for i in range(0, 32, 8)]
    subnet_mask = [str(int(bin_octet, 2)) for bin_octet in binary_mask]
    subnet_mask = '.'.join(subnet_mask)
    return subnet_mask


# 使用函数
subnet_mask = prefix_to_subnet_mask(23)
print(subnet_mask)  # 输出子网掩码的点分十进制形式
