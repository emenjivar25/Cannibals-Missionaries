#! usr/bin/env python3.5
"""
BFS For cannibals / missionaries. A little long for one file but I didn't feel like breaking it up 

"""
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

        #check obvious
        if(self.lMissionary + self.rMissionary > gMISSIONARIES or self.lCannibal+self.rCannibal > gCANNIBALS):
            return False
        if(self.rMissionary < 0 or self.lMissionary < 0 or self.rCannibal < 0 or self.lCannibal < 0):
            return False

        #need to have missionaries >= cannibals on a given side
        if(self.rCannibal > self.rMissionary and self.rMissionary > 0):
            returna
CC False

        if(self.lCannibal > self.lMissionary and self.lMissionary > 0):
            return False

        return True

#for printing output
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
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

#Expand a node to all possible moves
    def getNeighbors(self):
        retList = []
        if self.state.boat == 'r':
            #1 Missionary
            newState = State(self.state.lMissionary+1, self.state.rMissionary-1, self.state.lCannibal, self.state.rCannibal, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            #1 Cannibal

            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal+1, self.state.rCannibal-1, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            #1 Missionary 1 Cannibal
            newState = State(self.state.lMissionary+1, self.state.rMissionary-1, self.state.lCannibal+1, self.state.rCannibal-1, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            #2 Missionaries
            newState = State(self.state.lMissionary+2, self.state.rMissionary-2, self.state.lCannibal, self.state.rCannibal, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            #2 Cannibals
            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal+2, self.state.rCannibal-2, 'l')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

        else:
            # 1 Missionary
            newState = State(self.state.lMissionary - 1, self.state.rMissionary + 1, self.state.lCannibal, self.state.rCannibal, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            # 1 Cannibal
            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal - 1, self.state.rCannibal + 1, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            # 1 Missionary 1 Cannibal
            newState = State(self.state.lMissionary - 1, self.state.rMissionary + 1, self.state.lCannibal - 1, self.state.rCannibal + 1, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            # 2 Missionaries
            newState = State(self.state.lMissionary - 2, self.state.rMissionary + 2, self.state.lCannibal, self.state.rCannibal, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

            # 2 Cannibals
            newState = State(self.state.lMissionary, self.state.rMissionary, self.state.lCannibal - 2, self.state.rCannibal + 2, 'r')
            newNode = Node(newState, self)
            if newNode.state.isValid():
                retList.append(newNode)

        return retList
    
#find path taken to goal node, order it correctly
    def rollback(self):
        path = []
        pNode = self
        while pNode.parent != None:
            path.append(pNode.state)
            pNode = pNode.parent
        path.reverse()
        for p in path:
            print(p)
            print()


#Breadth first search

def mySearch():

    exset = set()
    start = State(gMISSIONARIES, 0, gCANNIBALS, 0, 'l')
    root = Node(start, None)
    frontier = []
    frontier.append(root)
    while frontier:
        newnode = frontier.pop(0)
        if newnode.state.finished():
            newnode.rollback()
            exit(0)
        exset.add(newnode)
        neighbors = newnode.getNeighbors()
        for n in neighbors:
            if (n not in exset) or (n not in frontier):
                frontier.append(n)


def main():
    mySearch()


if __name__ == "__main__":
    main()
