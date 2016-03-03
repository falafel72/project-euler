def readFile():
    f = open("Euler13 Numberfile.txt","r")
    lines = f.readlines()
    total = 0
    for i in range(len(lines)):
        total += int(lines[i])
    return str(total)[0:10]
  
