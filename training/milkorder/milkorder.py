with open("milkorder.in", 'r') as fin:
    numofcows, numhier, wish = map(int, fin.readline().split())
    if numhier != 0:
        hierarchy = list(map(int, fin.readline().split()))
    if wish != 0:
        wishlist = []
        for times in range(wish):
            wishlist.append(list(map(int, fin.readline().split())))
cowToPos = {}

print(wishlist)


'''
for i in len(wishlist):
    cowToPos[wishlist[i][0]] = wishlist[i][1]
posToCow = {x:0 for x in range(1, numofcows+1)}

for i in len(numhier):
    cowtoPos[numhier[i][0]] = numhier[i][1] 




print(wishlist)
print(hierarchy)
#empty dictionary
'''


#milkorder = {}

#{1:3, 2:0, 3:5, 4:0, 5:0, 6:0  }



''' 
#requirements = str("milkorder.in")

#hierarchy and special order categorized from parts of input 
hierarchy = range of requirements(0) to requirements(5)    

special_order = range of requirements(6) to requirements(9)

#special order first
for x in special_order 
    add to milk_order val2 greatest to val2 least 

#afterwards, THEN you can add hierarchy
for x in hierarchy
    if x(1) order > x(2) order 
    add to milk_order 
else 
    if x(2) order > x(3) order
    add to milk_order

'''