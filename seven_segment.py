#Imports regular expression module
import re

#Opens the word list and creates a list as a variable
file = open('words.txt', 'r')
file_content = file.read()
list = file_content.split('\n')

#Specifies the banned words in a regex
banned = re.compile("[gkmqvwxzio]")
#Creates a dictionary that stores words and their lengths
longest_acceptable = {'a': 1}

#Iterates through all words and adds them to the
#dictionary if there are no banned letters in them
#and if they aren't smaller than the biggest word.
for item in list:
    if banned.search(item) != None:
        continue
    elif len(item) < max(longest_acceptable.values()):
        continue
    else:
        longest_acceptable[item] = len(item)

#Stores the largest length as an int
biggest = max(longest_acceptable.values())
#Creates an empty string for storing the final result
longest_words = ""

#Iterates through dictionary and removes the words that
#are not the longest that have crept thorugh the cracks.
for k, v in longest_acceptable.items():
    if v == biggest:
        longest_words += k + '\n'

#Prints the final result
print(longest_words)

#Closes the file
file.close()
