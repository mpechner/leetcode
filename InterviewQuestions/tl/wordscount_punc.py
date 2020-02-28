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

for aword, occur in words.items():
    print("%d  %s" % (occur, aword))
