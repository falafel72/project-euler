def factorial(num):
    total = 1
    for i in range(2,num+1): total *= i
    return total

def digitSum(num):
    return sum([int(i) for i in list(str(num))])
