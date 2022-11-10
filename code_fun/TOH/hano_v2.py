#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'


### 1、2、3号 一共3个柱子  1 + 2 + 3 =6 

    
    

def hanoi(numRings, startPeg, endPeg):
    numMoves = 0
    if numRings == 1:
        print("from", startPeg, "to", 6-startPeg-endPeg, "move", numRings  )
        print("from", 6-startPeg-endPeg, "to",startPeg , "move", numRings )
        numMoves += 2
    else:
        print("from", startPeg, "to", endPeg, "move", numRings )
        numMoves += hanoi(numRings-1, startPeg, 6-startPeg-endPeg)
        print("from", startPeg, "to", endPeg, "move", numRings )
        numMoves += 1
        numMoves += hanoi(numRings-1, 6-startPeg-endPeg, startPeg)
    return numMoves




if __name__ == "__main__":
    numMoves = hanoi(5, 1, 3)
    print("move:", numMoves)