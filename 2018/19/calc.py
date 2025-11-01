U=[2, 5, 1055137, 10, 2110274, 5275685, 10551370,1]
su = 0
for x in U:
    for y in U:
        if x * y == 10551370:
            su += x
print(su)
