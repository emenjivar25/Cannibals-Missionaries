#! usr/bin/env python3.5

import random
import time
import sys
from collections import deque

gMISSIONARIES = 3
gCANNIBALS = 3
gBOATSIZE = 2


class State (object):
    def __init__(self, lmiss, rmiss, lcann, rcann, boatloc):
        self.lMissionary = lmiss
        self.rMissionary = rmiss
        self.lCannibal = lcann
        self.rCannibal = rcann
        self.boat = boatloc

    #see if we're finished
    def finished(self):
        if (self.rCannibal == gCANNIBALS and self.rMissionary == gMISSIONARIES):
            return True
        return False

    #check if state is valid according to problem description
    def isValid(self):

        #need a boat
        if(self.lMissionary + self.lCannibal == 0 and self.boat == 'r'):
            return False

        if(self.rMissionary + self.rCannibal == 0 and self.boat == 'l'):
            return False

        #need to have missionaries >= cannibals on a given side
        if(self.rCannibal > self.rMissionary):
            return False

        if(self.lCannibal > self.rMissionary):
            return False

        return True


    def __str__(self):
        list = []
        list.append('C' * self.lCannibal)
        list.append(' ')
        list.append('M' * self.lMissionary)
        if (self.boat == 'l'):
            list.append("_\__/_______________")
        else:
            list.append("_______________\__/_")
        list.append('C' * self.rCannibal)
        list.append(' ')
        list.append('M' * self.rMissionary)
        s = ''.join(list)
        return s


class Node(object):
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


    def getNeighbors(self):
        retList = []
        #if(self.state.boat == 'r'):

        #else:


    def rollback(self):
        path = []
        pNode = self
        while(pNode.parent != None):
            path.append(pNode.state)
            pNode = pNode.parent
        path.reverse()
        for p in path:
            print(p)







def main():
    start = State(gMISSIONARIES, 0, gCANNIBALS, 0, 'l')




if __name__ == "__main__":
    main()

