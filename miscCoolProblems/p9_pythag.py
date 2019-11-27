import math
done = False
while not done:
    for i in range(1, 1000):
        for j in range(1, 1000):
            sqrt_c = math.sqrt(i**2+j**2)
            if int(sqrt_c) == sqrt_c:
                if sqrt_c + i + j == 1000:
                    done = True
                    print(i, j, sqrt_c)
                    break
