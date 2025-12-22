from aocd import data

f, d = data.split("\n\n")

f = [*sorted((tuple(map(int, k.split("-"))) for k in f.split("\n")))]


print(sum(any(a <= int(x) <= b for a, b in f) for x in d.split("\n")))


r = ans = 0

for a, b in f:
    ans += max(0, b - (r if r >= a else (a - 1)))
    r = max(r, b)

print(ans)
