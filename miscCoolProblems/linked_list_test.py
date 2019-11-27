

class node():
    def __init__(self):
        pass


a = node()
a.key = 1
b = node()
b.key = 2
a.node = b
b.node = b

print(a.key, b.key, a.node.key, b.node.key)
