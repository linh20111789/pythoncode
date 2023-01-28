
from array import array


t = open('AAPL_Group.txt', 'r').readlines()
listData = []
listData2020 = []
listData2021 = []


listvolume = []
MaxVolume = 0
MinVolume = 100000000000
LowestOpen = 100000000000
HighestClose = 0
MaxVolumeDate = ''
MinVolumeDate = ''
LowestOpenDate = ''
HighestCloseDate = '' 


listColume = []

for n in t:
    line = n.strip()
    print(line)
    listData.append(line)



# print("listData")
# print(listData)

for lineData in listData:
    # print ("lineData ", lineData)
    # print ("lineData len", len(lineData))
    # print(lineData.split(','))
    arrayLine = lineData.split(',')


    YearData = arrayLine[0]

    listvolume.append(arrayLine[6]) 
    print(arrayLine[0])
    if YearData.find("2020-")!= -1:
        listData2020.append(lineData)
    elif YearData.find("2021-")!= -1:
        listData2021.append(lineData)
 
    #print(i.count(','));

# print("listData2020")
# print(listData2020)

for lineData in listData2020:
    arrayLine = lineData.split(',')
    
    
    if (MaxVolume <= int(arrayLine[6])):
        MaxVolume = int(arrayLine[6])
        MaxVolumeDate = arrayLine[0]
        # print("MaxVolume :", MaxVolume)
    if (MinVolume >= int(arrayLine[6])):
        MinVolume= int(arrayLine[6])
        MinVolumeDate = arrayLine[0]
        # print("MinVolume :", MinVolume)

    if (LowestOpen >= float(arrayLine[1])):
        LowestOpen = float(arrayLine[1])
        LowestOpenDate = arrayLine[0]
        # print("LowestOpen :", LowestOpen)

    if (HighestClose <= float(arrayLine[4])):
        HighestClose = float(arrayLine[4])
        HighestCloseDate = arrayLine[0]
        # print("HighestClose :", HighestClose)


print("MaxVolume final :", MaxVolume)       
print("MaxVolumeDate final :", MaxVolumeDate)       

print("MinVolume final :", MinVolume)       
print("MinVolumeDate final :", MinVolumeDate) 


print("LowestOpen final :", LowestOpen)       
print("LowestOpen Date final :", LowestOpenDate)


print("HighestClose final :", HighestClose)       
print("HighestClose Date final :", HighestCloseDate)
# print("listData2021")
# print(listData2021)


# print("listData2022")
# print(listData2022)


# my_file = open("AAPL_Group.txt", "r")
# content = my_file.read()
# print(content)
# content_list = content.split(",")
# my_file.close()
# print(content_list)

# listData = []
# with open("AAPL_Group.txt") as fileobject:
#     for line in fileobject:
#         print(line)
#         listData.append(line)

# print("listData")
# print(listData)


# listData = []
# from collections import deque
# with open("AAPL_Group.txt") as f:
#     for line in deque(f, maxlen=5000):
#         print(line)
#         listData.append(line)

# print("listData")
# print(listData)        

# with open('readme.txt', 'w') as f:
#     for line in listData:
#         f.write(line)
#         f.write('\n')
