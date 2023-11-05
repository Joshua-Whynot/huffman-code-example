#imports
import heapq
from node import Node

#huffman coding program using linked list and heap queue
#author: Joshua Whynot

#main function
def main():
    #ask if user would like to provide their own input
    choice = input("Would you like to use the sample data input?(Y/N): ")
    choice = choice.upper()
    if choice != 'Y':
        string_array = getUserInput()
        input_dict = count_frequency(string_array)
        chars, frequencies = dict_to_arrays(input_dict)
    elif choice == 'Y':
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #this is sample data
        frequencies =  [77, 17, 32, 42, 120, 24, 17, 50, 76, 4, 7, 42, 24, 67, 67, 20, 5, 59, 67, 85, 37, 12, 22, 4, 22, 2]
    
    nodes = []
 
    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(frequencies[x], chars[x]))
 
    while len(nodes) > 1:
 
        # sort all the nodes in ascending order
        # based on their frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
    
        # assign directional value to these nodes
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = Node(left.frequency+right.frequency, left.char+right.char, left, right)
    
        heapq.heappush(nodes, newNode)
 
    # create dictionary to store characters and codes
    codeDict = {}
    getCodes(nodes[0], codeDict)
    codeDict = sortDictionary(codeDict)
    # add frequency of each letter to dictionary
    output(codeDict, frequencies)
    



#get user input as list
def getUserInput():
    return list(input('Enter string to be encoded: '))
    
#get frequency 
def count_frequency(array):
    freq = {} #dictionary init
    for item in array: #loop through array and count frequency of each character and insert the frequency and characters as the key and value pairs.
        if item in freq: 
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

#create arrays of non repeated characters and their frequencies with the indexes matching.
def dict_to_arrays(d):
    keys = [key for key in d.keys()]
    values = [value for value in d.values()]
    return keys, values

#get our codes (path) and add it to a dictionary along with its character
def getCodes(node, dct, value=''):
    newValue = str(node.code) + value #get huffman code for current node
    #check if node is an edge node, if not traverse inside it
    if(node.left):
        getCodes(node.left, dct, newValue)
    if(node.right):
        getCodes(node.right, dct, newValue)
    #if its an edge node add char and code value to dictionary
    if(not node.left and not node.right):
        #make path value a string so we can reverse the number using extended string slicing
        stringvalue = str(newValue)
        stringvalue = stringvalue[::-1]
        #add char and value to dictionary for use in output
        dct[node.char] = stringvalue
    
#function to sort a dictionary alphabetically (Default sort)
def sortDictionary(dct):
    sortedKeys = sorted(dct.keys())
    sorted_dct = {}
    for key in sortedKeys:
        sorted_dct[key] = dct[key]
    return sorted_dct

def output(dct, frequency):
    i = 0 #used for getting correct freq from freq array
    #header text
    print(' Letter      Frequency           Code        Length          Freq X Len')
    print('--------  ---------------- ------------- ---------------- ----------------')
    weightedMin = 0 #init weighted minimum path length
    #loop through each key in dictionary
    for key in dct:
        #get code
        code = dct[key]
        freqlen = frequency[i] * len(code) #multiply frequency by code length to get freq x len
        #output data for current key (char, freq, code, len, freq x len)
        print('   {}\t\t{}\t\t{}     \t{}\t\t{}'.format(key, frequency[i], code, len(code), freqlen))
        weightedMin += freqlen #add freqlen to min path len
        i += 1 #increment
    print('The weighted minimum path length is:', weightedMin) #output min path len


if __name__ == '__main__':
    main()