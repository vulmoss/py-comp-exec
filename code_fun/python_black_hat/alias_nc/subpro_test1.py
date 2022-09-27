#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/9/27 22:45
# @Author   : VulMoss
# @Site     : 
# @File     : subpro_test1.py
# @Software : PyCharm

import subprocess

retcode = subprocess.call(["ls","-l"])
print(retcode)