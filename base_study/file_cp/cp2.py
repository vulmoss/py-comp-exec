#!/usr/bin/env python3

import sys

def copy_l_file(src_file,dst_file):
    with open(src_file,'r') as srcfile:
        with open(dst_file,'a') as dstfile:
            for i,line in enumerate(srcfile.readlines()):
                dstfile.write(str(i+1))
                dstfile.write(' ')
                dstfile.write(line)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_l_file(sys.argv[1],sys.argv[2])
    else:
        print("Parameter Error")
    sys.exit(0)



