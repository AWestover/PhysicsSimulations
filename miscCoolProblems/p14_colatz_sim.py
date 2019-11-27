#cd Dropbox\Python\atomProjects\euler
"""
The Colatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

"""


# Colatz conjecture is that all sequences eventually go to 1.

# print out how the sewuence happends
def display_colatz_sequence(seed):
    n = seed
    while n > 1:
        print(n, end=" -> ")
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
    print(n)

# recursively find the length of each chain as it converges to 0. (It will probably not go up into an infinite loop, but the colatz conjecture is still not proven...)
def colatz_length_to_one(seed):
    n = seed
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return colatz_length_to_one(n / 2) + 1
        elif n % 2 == 1:
            return colatz_length_to_one(3 * n + 1) + 1


display_colatz_sequence(837799)
input("How do you like that?")

# run parameters
max_range = 1000000
max_length = 1
found_at = 1

# loop through numbers
for i in range(1, max_range):
    c = colatz_length_to_one(i)
    if c > max_length:
        print("New max of {} was found at {}".format(c, i))
        found_at = i
        max_length = c

print("Max length of {} was found at n = {}".format(max_length, found_at))
