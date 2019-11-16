'''
ID: arcaand2
LANG: PYTHON3
TASK: ride
'''

with open('ride.in', 'r') as fin:
    line1 = [x for x in fin.readline().rstrip()]
    line2 = [x for x in fin.readline().rstrip()]

number1 = [ord(line1[x])-ord('A')+1 for x in range(len(line1))]

number2 = [ord(line2[x])-ord('A')+1 for x in range(len(line2))]


result1 = 1
result2 = 1
    
for x in number1: 
    result1 *= x
result1 = result1 % 47
for x in number2:
    result2 *= x
result2 = result2 % 47
with open('ride.out', 'w') as fout:
    if result1 == result2:
        print('GO', file=fout)
    else:
        print('STAY', file=fout)