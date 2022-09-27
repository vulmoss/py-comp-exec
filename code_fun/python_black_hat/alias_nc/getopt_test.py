import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], "-h-f:-v", ["help", "filename=", "version"]) #f 和 filename后必须有附件的参数
for opt, value in opts:
    if opt in ("-h", "--help"):
        print("[*] Help Info")
        exit(1)
    if opt in ("-v", "--version"):
        print("[*] Version is 1.0")
        exit(1)
    if opt in ("-f", "--filename"):
        filename = value
        print("[*] Filename is", filename)
        exit(1)
