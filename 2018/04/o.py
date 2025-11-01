from datetime import datetime, timedelta
import re
import typing
def lmap(func, *iterables):
	return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]:
	return lmap(int, re.findall(r"-?\d+", s))
N = 986
l = []
for x in range(N):
	u = input()
	date = u[6:17]
	inf = u[19: ]
	datetime_object = datetime.strptime("1518-" + date, '%Y-%m-%d %H:%M');
	l.append((datetime_object, inf))
l.sort()
cur = 0
pre = None
amt = {}
for dat, inf in l:
	if "Guard" in inf:
		cur = ints(inf)[0]
		if not cur in amt.keys():
			amt[cur] = [0, dict()]
			for x in range(60):
				amt[cur][1][x] = 0
	elif "wakes" in inf:
		lol = pre
		asd = timedelta(minutes=1)
		while lol < dat:
			amt[cur][0] += 1
			amt[cur][1][lol.minute] += 1
			lol += asd
	else:
		assert "falls" in inf
	pre = dat
best_amt = -1
best_guard = -1
best_minute = -1
for id, b in amt.items():
	for c, d in b[1].items():
		if d > best_amt:
			best_amt = d
			best_minute = c
			best_guard = id
print(best_minute * best_guard)
