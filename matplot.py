import matplotlib.pyplot as plt
import csv

vals = list()
dedingen = list()

with open ('proc.csv', newline='') as defile:
    read = csv.reader(defile, delimiter=' ', quotechar='|')
    for ding in read:
        extra = str(ding[1])
        extra = extra.replace('"', '')
        extra = extra.split(',')
        vals.append(extra[1])
        print(extra)
for ding in vals:
    extra = ding.split('.')
    dedingen.append(int(extra[0]))

plt.plot([1,2,3,4,5,6,7],dedingen)

plt.title('CPU gebruik')
plt.xlabel('seconden')
plt.ylabel('gebruik')
plt.show()
