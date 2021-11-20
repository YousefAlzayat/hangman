import os
# Entering path of txt file to take words from such that it works as long as the file is in the same folder as the python code
mainpath = os.path.dirname(os.path.abspath(__file__)) + "\\worddictionary.txt"
mainpath = mainpath.split("\\")
path = ""

for i in mainpath:

    if i != "worddictionary.txt":
        path = path + i + "/"

    else:
        path = path + i

word_list = []
words = open(path, 'r')
word_list = words.read().split("\n")
