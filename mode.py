from collections import Counter
import csv
with open('height-weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)

newdata=[]
for i in range(len(file_data)):
    num=file_data[i][1]
    newdata.append(float(num))
n=len(newdata)
data=Counter(newdata)
getmode=dict(data)
mode1=[]
mode2=[]
mode=[]
modeRange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurance in data.items():
    if 50<float(height)<60:
        modeRange['50-60']+=occurance
    elif 60<float(height)<70:
        modeRange['60-70']+=occurance
    elif 70<float(height)<80:
        modeRange['70-80']+=occurance
mode_range,mode_occurance=0,0
for range,occurance in modeRange.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance=[int(range.split('-')[0]),int(range.split('-')[1]),occurance]
        mode=float((mode_range[0]+mode_range[1])/2)
        print(f'Mode is ->{mode:2f}')