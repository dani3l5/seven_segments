import re

file = open('words.txt', 'r')
file_content = file.read()
list = file_content.split('\n')

banned = re.compile("[gkmqvwxzio]")
longest_acceptable = {'a': 1}

for item in list:
    if banned.search(item) != None:
        continue
    elif len(item) < max(longest_acceptable.values()):
        continue
    else:
        longest_acceptable[item] = len(item)

biggest = max(longest_acceptable.values())
longest_words = ""

for k, v in longest_acceptable.items():
    if v == biggest:
        longest_words += k + '\n'

print(longest_words)