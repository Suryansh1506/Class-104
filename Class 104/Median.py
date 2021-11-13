import csv
from types import new_class
with open("HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)

Newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    Newdata.append(float(num))

n=len(Newdata)
Newdata.sort()
if n % 2==0:
    median1=float(Newdata[n//2])
    median2=float(Newdata[n//2-1])
    median=(median1+median2)/2

else:
    median=Newdata[n//2]

print(median)