f = lambda x : (x // 3) - 2
u = list(map(lambda x : int(x.strip()), open('input').readlines()))
print(sum(map(f, u)))
