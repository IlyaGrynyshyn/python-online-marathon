def findPermutation(n, p, q):
    r = []
    list = 0
    for i in range(n):
        list = q[i]
        r.append(p.index(list)+1)
    return r
n = 5
p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]
print(findPermutation(n, p, q))