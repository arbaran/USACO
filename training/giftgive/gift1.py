 '''
ID: arcaand2
LANG: PYTHON3
TASK: gift1

'''
order = []
name = ""

with open('gift1.in') as fin: 
    num = int(fin.readline())
    for _ in range(num):
        order.append(fin.readline().rstrip())
    rawtransactions = fin.readlines()
transactions = []
values = {i: 0 for i in order}
for i in range(len(rawtransactions)):
    if rawtransactions[i].rstrip() in values:
        transactions.append(rawtransactions[i].rstrip())
    else:
        transactions.append(list(map(int, rawtransactions[i].rstrip().split())))
print(values)
print(transactions)
givemoney = False
for i in range(len(transactions)):
    if type(transactions[i]) is list:
        if transactions[i][1] != 0:
            amounttoadd = int(transactions[i][0]/transactions[i][1]) 
            amounttokeep = int(transactions[i][0]%transactions[i][1])
        else:
            amounttoadd = 0
            amounttokeep = 0
        values[name] -= transactions[i][0]-amounttokeep
        looping = transactions[i][1]
        if looping != 0:
            givemoney = True
        continue
    elif givemoney == False:
        name = transactions[i]
        continue
    elif givemoney == True:
        values[transactions[i]] += amounttoadd
        looping -= 1    
        print(values)
        if looping == 0:
            givemoney = False
with open('gift1.out', 'w') as fout:
    for i in order:
        print('%s %d' % (i, values[i]), file=fout)