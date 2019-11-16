#open file, put string into list 

with open('beads.in', 'r') as fin:
    N = int(fin.readline())
    necklace = fin.readline().strip() 

flatnecklace = necklace * 2 

print(flatnecklace)

maxResult = 0

for i in flatnecklace: 
    Wcounter = 0
    Rcounter = 0
    Bcounter = 0
    firstNonWhiteBead = False
    SecondColor = False
    result = 0 
    if i == 'w': 
        Wcounter += 1
        continue
        firstNonWhiteBead = True 
        if i == 'r':
            Rcounter += 1
            while i == 'r':
                Rcounter+= 1 
        else: 
            SecondColor = True
            while SecondColor == True:
                result = Rcounter + Wcounter
    else: 
        Bcounter += 1 
        if i == 'b' : 
            while i == 'b':
                Bcounter+= 1 
        else: 
            SecondColor = True
            while SecondColor == True:
                result = Bcounter + Wcounter
             

        
result = int(Rcounter + Bcounter)

maxresult = max(maxresult, result)

print(result)

#while loop of W... add to W counter
# once nonWletter is found... add to the r/b counter
# once secondcolor found... break. add w counter + r/b counter to get total number of that color.  


"""with open('beads.out', 'w') as Fout:
    
    Fout.write(str() + ' ')
    Fout.write(str() + '\n')""" 