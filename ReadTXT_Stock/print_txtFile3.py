
from array import array

listData = []
listData2020 = []
listData2021 = []


MaxVolume2020 = 0
MinVolume2020 = 100000000000
LowestOpen2020 = 100000000000
HighestClose2020 = 0
HighestMoAv2020 = 0
LowestMoAv2020 = 0

MaxVolumeDate2020 = ''
MinVolumeDate2020 = ''
LowestOpenDate2020 = ''
HighestCloseDate2020 = '' 
HighestMoAvMonth2020 = ''
LowestMoAvMonth2020 = ''

monthAverageList2020 = [0,0,0,0,0,0,0,0,0,0,0,0]
monthAverageListCount2020 = [0,0,0,0,0,0,0,0,0,0,0,0]

t = open('AAPL_Group.txt', 'r').readlines()


listColume = []

for n in t:
    line = n.strip()
    # print(line)
    listData.append(line)


for lineData in listData:

    arrayLine = lineData.split(',')


    YearData = arrayLine[0]

    # print(arrayLine[0])
    if YearData.find("2020-")!= -1:
        listData2020.append(lineData)
    elif YearData.find("2021-")!= -1:
        listData2021.append(lineData)

sum = 0
count = 0
for lineData in listData2020:
    arrayLine = lineData.split(',')
    
    
    if (MaxVolume2020 <= int(arrayLine[6])):
        MaxVolume2020 = int(arrayLine[6])
        MaxVolumeDate2020 = arrayLine[0]
        # print("MaxVolume :", MaxVolume)
    if (MinVolume2020 >= int(arrayLine[6])):
        MinVolume2020 = int(arrayLine[6])
        MinVolumeDate2020 = arrayLine[0]
        # print("MinVolume :", MinVolume)

    if (LowestOpen2020 >= float(arrayLine[1])):
        LowestOpen2020 = float(arrayLine[1])
        LowestOpenDate2020 = arrayLine[0]
        # print("LowestOpen :", LowestOpen)

    if (HighestClose2020 <= float(arrayLine[4])):
        HighestClose2020 = float(arrayLine[4])
        HighestCloseDate2020 = arrayLine[0]
        # print("HighestClose :", HighestClose)


    if arrayLine[0].find("-01-")!= -1:
        
        monthAverageList2020[0] = monthAverageList2020[0] + float(arrayLine[2])
        monthAverageListCount2020[0] = monthAverageListCount2020[0] + 1
        print("sum",monthAverageList2020[0] )
        print("count",monthAverageListCount2020[0])
        


print("MaxVolume final :", MaxVolume2020)       
print("MaxVolumeDate final :", MaxVolumeDate2020)       

print("MinVolume final :", MinVolume2020)       
print("MinVolumeDate final :", MinVolumeDate2020) 


print("LowestOpen final :", LowestOpen2020)       
print("LowestOpen Date final :", LowestOpenDate2020)


print("HighestClose final :", HighestClose2020)       
print("HighestClose Date final :", HighestCloseDate2020)
# print("listData2021")

