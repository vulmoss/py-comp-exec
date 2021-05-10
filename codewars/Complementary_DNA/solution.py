#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'



#DNA_strand ("ATTGC")

#DNA_strand ("GTAT")

def DNA_strand(dna):
    # code here
    covert = {
            "A" : "T",
            "T" : "A",
            "C" : "G",
            "G" : "C",
            }
    print( "".join(covert[i] for i in dna))
    return "".join(covert[i] for i in dna)

if __name__ == '__main__':
    DNA_strand('ATTGC')
    DNA_strand('GTAT')

