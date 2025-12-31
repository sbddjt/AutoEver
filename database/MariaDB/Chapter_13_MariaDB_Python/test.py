from itertools import groupby

s = 'aaaaabbbbbcccc'
l = max(groupby(s), key = lambda x : len(list(x[1])))
print(l[0])