
# puts a into the end of every array in l
def flood(l, a):
    out = []
    for i in range(0, len(l)):
        out.append(l[i] + [a])
    return out

# all possible combinations of elements in l of length depth, duplicates allowed
def fill_list(l, depth):
    out = [[le] for le in l]
    for i in range(0, depth - 1):
        pending = []
        for j in range(0, len(l)):
            cur = flood(out, l[j])
            for c in cur:
                pending.append(c)
        out = pending
    return out

# all arrays in a list are turned into integers
def propArrayToInt(arr):
    out = []
    for el in arr:
        c = [str(e) for e in el]
        c = "".join(c)
        c = int(c)
        out.append(c)
    return out