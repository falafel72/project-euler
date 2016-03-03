def selfpowers():
    total = 0
    for i in range(1,1000):
        total += (i**i)
        total %= 10**10
    return total
