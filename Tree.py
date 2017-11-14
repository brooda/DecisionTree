# simple binary tree
# in this implementation, a node is inserted between an existing node and the root

from Fuzziness import *
import numpy as np

class TreeNode():
    def __init__(self, etiquette, fuzziness):
        self.etiquette = etiquette
        self.left = None
        self.right = None
        self.fuzziness = fuzziness
        self.rate = 100

    def getEtiquette(self):
        return self.etiquette;

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right

    def insertRight(self,newNode):
        if self.right == None:
            self.right = newNode
        else:
            tree = newNode
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = newNode
        else:
            tree = newNode
            tree.left = self.left
            self.left = tree

    def getQuestions(self):
        if self.fuzziness == Fuzziness.LINEAR:
            return ("na pewno nie: 1, raczej nie: 2, nie wiem: 3, raczej tak: 4, na pewno tak: 5", [1, 2, 3, 4, 5],
                    [0, 25, 50, 75, 100])
        elif self.fuzziness == Fuzziness.SIGMOIDAL:
            return ("Na pewno tak: 100, na pewno nie: 1", list(reversed(range(1, 101))),
                    sigmoid())
        else:
            return ("Tak: 2, nie: 1", [1,2],
                    [0, 100])

    def setRate(self, rate):
        self.rate = rate

    def getRate(self):
        return self.rate

def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getEtiquette())
        printTree(tree.getRightChild())


def sigmoid():
    ret = [int(x) for x in list(np.round(100 / (1 + np.exp(-np.arange(100) / 10 + 5)), 0))]
    ret[0] = 0
    ret[-1] = 1
    return ret
