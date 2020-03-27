n = int(input())
foo = bar = 0
while n > 0:
    if n % 2 == 0:
        foo += 1
    else:
        bar += 1
    n = n // 10
print("четных %d, нечетных %d" % (foo, bar))