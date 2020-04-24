"""
Eratosphene
"""

def e_sieve(length):
    """ Classic method """
    sieve = [0] * length
    for i in range(length):
        sieve[i] = i
    sieve[1] = 0
    curr = 2

    while curr < length:
        if sieve[curr] != 0:
            j = curr * 2
            while j < length:
                sieve[j] = 0
                j = j + curr
        curr += 1

    result = [x for x in sieve if sieve[x] != 0]
    return result

print(e_sieve(30))
