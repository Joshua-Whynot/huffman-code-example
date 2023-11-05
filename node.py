class Node:
    def __init__(self, freq, char, left = None, right = None):
        #initialize vars for node
        self.left = left #pointer to left child (if exists)
        self.right = right #pointer to right child (if exists)
        self.frequency = freq #frequency of character from user input
        self.char = char #character being encoded
        self.code = '' #used for tree direction (0 for left 1 for right)
        

    #comparator method
    def __lt__(self, nxt):
        return  self.frequency < nxt.frequency

        