realspeed = []
bessiespeed = []
a = []
b = []
stuffthingy = [0]
with open('speeding.in', 'r') as fin:
    n, m = fin.readline().split()
    for x in range(int(n)):
        realspeed.append(list(map(int, fin.readline().split())))
    for x in range(int(m)):
        bessiespeed.append(list(map(int, fin.readline().split())))
for x in range(len(realspeed)):
    for y in range(realspeed[x][0]):
        a.append(realspeed[x][1])
for x in range(len(bessiespeed)):
    for y in range(bessiespeed[x][0]):
        b.append(bessiespeed[x][1])

for x in range(100):
    if b[x] > a[x]:
        stuffthingy.append(b[x]-a[x])
with open('speeding.out', 'w') as fout:
    print(max(stuffthingy), file=fout)

fout.close()
fin.close()
