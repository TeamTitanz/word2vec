with open("word.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line.rstrip())
del array[0]
print array
