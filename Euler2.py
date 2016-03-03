def fib():
    x = 0
    y = 1
    z = 0
    total = 0
    while z < 4000000:
        if z%2 == 0:
            total = total + z
        z = x + y
        x = y
        y = z
    return total
