
from array import array
from asyncio.windows_events import NULL
import sys

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

HighestmonthAverageList2020 = [0,0,0,0,0,0,0,0,0,0,0,0]
MAX_D = 100000000
LowestmonthAverageList2020 = [0,0,0,0,0,0,0,0,0,0,0,0]
monthAverageListCount2020 = [0,0,0,0,0,0,0,0,0,0,0,0]


def convertPo2Month(number):
    if number == 1:
        return "January"
    elif number == 2:
        return "February"
    elif number == 3:
        return "March" 
    elif number == 4:
        return "April"
    elif number == 5:
        return "May"
    elif number == 6:
        return "June" 
    elif number == 7:
        return "July"
    elif number == 8:
        return "August"
    elif number == 9:
        return "September" 
    elif number == 10:
        return "October"
    elif number == 11:
        return "November"
    elif number == 12:
        return  "December"
    else:
        return number



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


    for i in range(1,13):
        # print(i)
        if i==10 or i==11 or i ==12 :
            text = "-" + str(i) +"-"
        else:
            text = "-0" + str(i)  + "-"
        # print("texxt",text)    
        if arrayLine[0].find(text)!= -1:
            HighestmonthAverageList2020[i-1] = HighestmonthAverageList2020[i-1] + float(arrayLine[2])
            LowestmonthAverageList2020[i-1] = LowestmonthAverageList2020[i-1] + float(arrayLine[3])
            monthAverageListCount2020[i-1] = monthAverageListCount2020[i-1] + 1
            print("LowestmonthAverageList2020 ",LowestmonthAverageList2020 [i-1] )
            print("count",monthAverageListCount2020[i-1])


print("HighestmonthAverageList2020 final :", HighestmonthAverageList2020)      
print("LowestmonthAverageList2020 final :", LowestmonthAverageList2020)    
print("monthAverageListCount2020 final :", monthAverageListCount2020)

for i in range (len(monthAverageListCount2020)):
    if monthAverageListCount2020[i] != 0:
        HighestmonthAverageList2020[i] = HighestmonthAverageList2020[i]/monthAverageListCount2020[i]
        LowestmonthAverageList2020[i] = LowestmonthAverageList2020[i]/monthAverageListCount2020[i]

print("monthAverageList2020 new :", HighestmonthAverageList2020) 
print("monthAverageList2020 new :", max(HighestmonthAverageList2020)) 

print("LowestmonthAverageList2020 new :", LowestmonthAverageList2020) 
print("LowestmonthAverageList2020 new :", min(LowestmonthAverageList2020))

monthAverageList2020Max = [po for po in range(0, len(HighestmonthAverageList2020)) if HighestmonthAverageList2020[po] == max(HighestmonthAverageList2020)]
monthAverageList2020Min = [po for po in range(0, len(HighestmonthAverageList2020)) if LowestmonthAverageList2020[po] == min(LowestmonthAverageList2020) and LowestmonthAverageList2020[po] != 0 ]

print("monthAverageList2020 monthAverageList2020Max :", *monthAverageList2020Max)
print("monthAverageList2020 monthAverageList2020Max :", convertPo2Month(int(*monthAverageList2020Max) + 1))

print("monthAverageList2020 monthAverageList2020Min :", *monthAverageList2020Min)
print("monthAverageList2020 monthAverageList2020Min :", convertPo2Month(int(*monthAverageList2020Min) + 1))


# print("MaxVolume final :", MaxVolume2020)       
# print("MaxVolumeDate final :", MaxVolumeDate2020)       

# print("MinVolume final :", MinVolume2020)       
# print("MinVolumeDate final :", MinVolumeDate2020) 


# print("LowestOpen final :", LowestOpen2020)       
# print("LowestOpen Date final :", LowestOpenDate2020)


# print("HighestClose final :", HighestClose2020)       
# print("HighestClose Date final :", HighestCloseDate2020)
# print("listData2021")

