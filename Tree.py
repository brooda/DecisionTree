# simple binary tree
# in this implementation, a node is inserted between an existing node and the root

from Fuzziness import *

class TreeNode():
    def __init__(self, etiquette, fuzziness):
        self.etiquette = etiquette
        self.left = None
        self.right = None
        self.fizzuness = fuzziness

    def getEtiquette(self):
        return self.etiquette;

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right

    def insertRight(self,newNode):
        if self.right == None:
            self.right = TreeNode(newNode)
        else:
            tree = TreeNode(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = TreeNode(newNode)
        else:
            tree = TreeNode(newNode)
            tree.left = self.left
            self.left = tree


def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getEtiquette())
        printTree(tree.getRightChild())
