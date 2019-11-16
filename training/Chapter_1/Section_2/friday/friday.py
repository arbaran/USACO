'''
ID: arcaand2
LANG: PYTHON3
TASK: friday

'''

days = [1, 0, 0, 0, 0, 0, 0]

with open('friday.in', 'r') as fin:
    N = int(fin.readline())

monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def LeapYear(year):
    global monthdays
    if year % 4 == 0:
        monthdays[1] = 29
        if year % 100 == 0 and year % 400 != 0: 
            monthdays[1] = 28
    else: 
        monthdays[1] = 28

finalyear = 1900+N
next13 = 13
for year in range(1900, finalyear):
    LeapYear(year)
    
    for i, mdays in enumerate(monthdays):
        if year == finalyear - 1 and i == 11:
            break
        next13 += mdays
        if next13 % 7 == 0:
            days[1] += 1
        if next13 % 7 == 1:
            days[2] += 1
        if next13 % 7 == 2:
            days[3] += 1
        if next13 % 7 == 3:
            days[4] += 1
        if next13 % 7 == 4:
            days[5] += 1
        if next13 % 7 == 5:
            days[6] += 1
        if next13 % 7 == 6:
            days[0] += 1 

#print(days)

with open('friday.out', 'w') as Fout:
    for i, day in enumerate(days):
        if i < 6:
            Fout.write(str(day) + ' ')
        else:
            Fout.write(str(day) + '\n')

    