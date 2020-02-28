import fileinput


fi = fileinput.FileInput(files=("words.txt"))
words = {}
for line in fi:
    for aword in line.split():
        #print(aword)
        if aword in words:
            words[aword] +=1
        else:
            words[aword] = 1

for aword, occur in words.items():
    print("%d  %s" % (occur, aword))
