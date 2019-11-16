from itertools import chain

fin = open ('paint.in', 'r')
fout = open ('paint.out', 'w')
ab = list(map(int, fin.readline().split()))
cd = list(map(int, fin.readline().split()))
l = [ab, cd]
l = sorted(l)
print(l)
#four.write (str(sum) + '\n')


flat = [val for sublist in l for val in sublist] 
print(flat)

a = flat[0]
b = flat[1]
c = flat[2]
d = flat[3]

if b < c: 
    print((b-a)+(d-c), file=fout)
    print((b-a)+(d-c))
else: 
    print(max(flat)-min(flat), file=fout)
    print(max(flat)-min(flat))


fout.close()
