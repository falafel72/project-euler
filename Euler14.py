collatzDict = {}

def collatz(num):
    global collatzDict
    numList = [num]
    counter = 0
    while num != 1:
        if num in collatzDict:
            return counter + collatzDict[num]
        if num % 2 == 0:
            num = num//2
        else:
            num = 3*num+1
        counter += 1
        numList = numList + [num]
    return len(numList)


def longestCollatz(maxNum):
    longestSeqNum = 0
    longestSeq = 0
    for i in range(1,maxNum+1):
        collatzDict[i] = collatz(i)
    return max(collatzDict,key=collatzDict.get)

#NOT MY CODE
def fill(d, k):
    if not k % 2:
        if k/2 not in d:
            fill(d,k/2)
        d[k] = 1 + d[k/2]
    else:
        o = 3*k+1
        if o not in d:
            fill(d,o)
        d[k] = 1 + d[o]
d = {1:1}
for i in range(2,1000000):
    fill(d,i)
highkey = 0
highv = 0
for (k,v) in d.items():
    if v > highv and k < 1000000:
        highv = v
        highkey = k
print(highkey)
