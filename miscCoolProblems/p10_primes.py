import math


def is_prime(n):
    for i in range(2, 1 + int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

psum = 0
for i in range(2, 2*10**6):
    if is_prime(i):
        psum += i

print(psum)
