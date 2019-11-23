'''
ID: arcaand2
LANG: PYTHON3
TASK: beads
'''

#open file, put string into list 

with open('beads.in', 'r') as fin:
    N = int(fin.readline())
    necklace = fin.readline().strip() 

flatnecklace = necklace * 2 

#print(flatnecklace)

maxResult = 0

for i in range(len(flatnecklace)): 
    firstcolor = None
    secondcolor = None
    currentmax = 0
    for j in range(i, len(flatnecklace)):
        if flatnecklace[j] == 'w':
            currentmax += 1
        else:
            # break out the inner loop when we got the 3rd color
            if secondcolor != None and secondcolor != flatnecklace[j]:
                break
            # We're collecting 1st and/or 2nd color beads
            if firstcolor == None: 
                firstcolor = flatnecklace[j]
                currentmax += 1
            else:
                if firstcolor == flatnecklace[j]:
                    currentmax += 1
                else:
                    secondcolor = flatnecklace[j]
                    currentmax += 1 
    
    if currentmax == len(necklace):
        maxResult = currentmax 
        break 
    maxResult = max(currentmax, maxResult)

#print(maxResult)

with open('beads.out', 'w') as Fout:
    Fout.write(str(maxResult) + '\n')