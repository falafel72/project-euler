import math

def sieve(maxVal):
    nums = [i for i in range(2,maxVal+1)]

    notprimes = [j for i in range(2,int(maxVal**(1/4))) \
                 for j in range(i*2,int(math.sqrt(maxVal)),i)]
    primes = [i for i in range(2,int(math.sqrt(maxVal))) if i not in notprimes]

    for i in primes:
        filt = filter(lambda x:(x%i!=0 or x == i),nums)
        nums = [i for i in filt]
    return nums
