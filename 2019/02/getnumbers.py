import re
from fileinput import input as i
s = ''.join(i())
s = s.split('\n')
for line in s:
	line = line.strip()
	lol = list(map(int, re.findall(r'[-\d]+', line)))
	lol = [str(x) for x in lol]
	line = ' '.join(lol)
	print(line)
