with open('teleport.in', 'r') as thing:
    a, b, x, y = thing.readline().split()

a = int(a)
b = int(b)
x = int(x)
y = int(y)

method1 = abs(x-a)+abs(b-y)

method2 = abs(b-a)

method3 = abs(y-a)+abs(b-x) 

result = min(method1, method2, method3)

print(result)
