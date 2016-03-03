import math

def factor(num):
    primes = genPrimes(num)
    factors = []
    factors.append(1)
    factors.append(num)
    while num > 1 and num not in primes:
        for prime in primes:
            if num % prime == 0:
                factors.append(prime)
                num = num//prime
                factors.append(num)
        if num == 1 or num in primes: break
    for i in set(factors):
        if factors.count(i) > 1:
            for j in range(2,factors.count(i) + 1):
                factors.append(i**j)
    return set(factors)


def genPrimes(num):
    notPrime = [n for factor in range(2,int(math.sqrt(num))) for n in range(factor*2,num,factor)]
    return [i for i in range(2,num) if i not in notPrime]
