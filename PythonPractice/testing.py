i = [(3, 'x1'), (5, 'x3'), (2, 'x2')]

print(' '.join('%s=%s' % (k, v) for (v, k) in i))

for x, y in i:
    print("%s=%s" % (y, x))

print(' '.join("%s=%d" % (y, x) for x, y in i))


def my_function(x):
    return x[::-1]


mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
