def sumOfSquares(num):
    total = 0
    for i in range(1,num+1):
        total = total+(i**2)
    return total

def squareOfSum(num):
    total = 0
    for i in range(1,num+1):
        total = total+i
    return total**2
