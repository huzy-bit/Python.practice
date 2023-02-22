#taking morse code as a string
a = str(input("type your morse code"))
print(a)
allwords = a.split()
#finding the lenght of the string so for loop can run only that much time
length = len(allwords)
print(length)
print(allwords)
b = []

for i in range(len(allwords)):
    #if else statements to check the morse code and append command for the updating the list
    if allwords[i] == "._":
        b.append("A")
    elif allwords[i] == "_...":
        b.append("B")
    elif allwords[i] == "_._.":
        b.append("C")
    elif allwords[i] == "_..":
        b.append("D")
    elif allwords[i] == ".":
        b.append("E")
    elif allwords[i] == ".._.":
        b.append("F")
    elif allwords[i] == "__.":
        b.append("G")
    elif allwords[i] == "....":
        b.append("H")
    elif allwords[i] == "..":
        b.append("I")
    elif allwords[i] == ".___":
        b.append("J")
    elif allwords[i] == "_._":
        b.append("K")
    elif allwords[i] == "._..":
        b.append("L")
    elif allwords[i] == "__":
        b.append("M")
    elif allwords[i] == "_.":
        b.append("N")
    elif allwords[i] == "___":
        b.append("O")
    elif allwords[i] == ".__.":
        b.append("P")
    elif allwords[i] == "__._":
        b.append("Q")
    elif allwords[i] == "._.":
        b.append("R")
    elif allwords[i] == "...":
        b.append("S")
    elif allwords[i] == "_":
        b.append("T")
    elif allwords[i] == ".._":
        b.append("U")
    elif allwords[i] == "..._":
        b.append("V")
    elif allwords[i] == ".__":
        b.append("W")
    elif allwords[i] == "_.._":
        b.append("X")
    elif allwords[i] == "_.__":
        b.append("Y")
    elif allwords[i] == "__..":
        b.append("Z")
#joining the list back to string
X="".join(b)
print(X)