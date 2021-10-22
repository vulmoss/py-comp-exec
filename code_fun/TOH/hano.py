#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

def hanoi(numRing, startPeg, endPeg):
    numMoves = 0
    if numRing > 0 :
        numMoves += hanoi(numRing - 1,startPeg,6 - startPeg - endPeg)
        print('Move ring',numRings,'from peg', startPeg, ' to peg', endPeg)
        numMoves += 1
        numMoves += hanoi(numRings -1 ,6 - startPeg - endPeg, endPeg)
    return numMoves
