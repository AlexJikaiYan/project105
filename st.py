import csv
import math
with open("data105.csv") as f:
   reader=csv.reader(f) 
   filedata=list(reader)
data=filedata[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2  
    squared_list.append(a)
sum=0
for i in squared_list:
    sum=sum+i
result=sum/(len(data)-1) 
sd=math.sqrt(result) 
print(sd) 