import fileinput
import re

fi = fileinput.FileInput(files=("words.txt"))
words = {}
for line in fi:
    for aword in re.split(r"\W+", line):
        if aword.strip() == '':
            continue
        #print(aword)
        if aword in words:
            words[aword] +=1
        else:
            words[aword] = 1
occurance = {}
for aword, occur in words.items():
    if occur in occurance:
        occurance[occur].append(aword)
    else:
        occurance[occur] = [aword]

key_list = list(occurance.keys())
key_list.sort(reverse=True)
for occur in key_list:
    for aword in occurance[occur]:
        print("%d %s" % (occur, aword))
