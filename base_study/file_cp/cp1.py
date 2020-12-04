#!/usr/bin/env python3

import sys

def copy_file(src_file,dst_file):
    with open(src_file,'r') as srcfile:
        with open(dst_file,'w') as dstfile:
            dstfile.write(srcfile.read())

if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1],sys.argv[2])
    else:
        print("Parameter Error")
        print(sys.argv[0],"srcfile dstfile")
        print(sys.exit(-1))
    sys.exit(0)
