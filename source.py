#! usr/bin/env python

import random
import time
import sys
from collections import deque


class State (object):
    def __init__(self, lmiss, rmiss, lcann, rcann, boatloc):
        self.lMissionary = lmiss
        self.rMissionary = rmiss
        self.lCannibal = lcann
        self.rCannibal = rcann
        self.boat = boatloc

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






def main():
    start = State(3, 0, 3, 0, 'l')


if __name__ == "__main__":
    main()

