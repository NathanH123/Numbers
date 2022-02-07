from re import M
import pandas as pd
import csv

with open("height-weight.csv") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []
for i in range(len(filedata)):
   in_number = filedata[i] [1]
   newdata.append(float(in_number))
n = len(newdata)
total = 0
for x in newdata :
    total +=x
mean = total/n
print(mean)