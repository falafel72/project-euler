def smallestMultiple():
    i = 200
    primes = [2,3,4,5,7,9,11,13,16,17,19]
    primes.reverse()
    while True:
        for j in primes:
            if i % j == 0 and j == 2: return i
            else:
                i += 20 
                break

def smallestMultiple2():
    i = 1
    #while True:
        #if (i % 2 == 0 and i % 3 == 0

def primeTest():
    num = 600851475143
    factor = 2

    while num != 1:
        if num % factor == 0:
            print(factor)
            num = num/factor
        else:
            factor += 1
