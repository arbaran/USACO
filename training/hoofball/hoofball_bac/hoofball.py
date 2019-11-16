lines = []
with open("hoofball.in") as fInput:
    lines = fInput.readlines()

cowAmount = lines[0]
cowPosition = list( int(i) for i in lines[1].split())
cowPosition.sort()

distances = []
for i in range(1, len(cowPosition)):
    distances.append(cowPosition[i] - cowPosition[i-1])


print(cowAmount, cowPosition, distances)

directions = [] 

directions.append('right')
for i in range(len(distances)):
    if d[i+1] < d[i]
      directions.append('right')
    directions.append()


    

"""
distance = []
distance1 = int[1]-int[0]
distance2 = 
"""


#[sorted(str.lines[0].split())]