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

N=len(Newdata)
sum=0
for x in Newdata:
    sum=sum+x

Mean=sum/N

print("Mean="+str(Mean))
