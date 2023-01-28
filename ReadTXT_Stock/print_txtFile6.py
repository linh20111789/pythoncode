
from array import array
from asyncio.windows_events import NULL
import os, time, sys 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

listData = []
listData2020 = []
listData2021 = []

MAX_DEFAULT = 1000000000

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


def OpenInputFile(filename):
    ld = []
    try:
        FileR = open(filename, 'r').readlines()
        for n in FileR:
            line = n.strip()
            ld.append(line)
        return ld    
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        print ("Unexpected error:", sys.exc_info()[0])


def Analysis (data):
    MaxVolume = 0
    MinVolume = 100000000000
    LowestOpen = 100000000000
    HighestClose = 0
    MaxVolumeDate = ''
    MinVolumeDate = ''
    LowestOpenDate= ''
    HighestCloseDate = '' 
    HighestMoAvMonth = ''
    LowestMoAvMonth = ''

    monthAverageMax =0 
    monthAverageMin = 0 
    monthAverageMaxValue =  0
    monthAverageMinValue = 0

    HighestmonthAverageList = [0,0,0,0,0,0,0,0,0,0,0,0]

    LowestmonthAverageList = [0,0,0,0,0,0,0,0,0,0,0,0]
    monthAverageListCount = [0,0,0,0,0,0,0,0,0,0,0,0]

    listMonthAverageVolume = [0,0,0,0,0,0,0,0,0,0,0,0]
    listMonthAverageCloseValue= [0,0,0,0,0,0,0,0,0,0,0,0]

    analysisList = []
    volumeAnualAverageList = []
    for lineData in data:
        arrayLine = lineData.split(',')

        volumeAnualAverageList.append(int(arrayLine[6]))
        
        if (MaxVolume <= int(arrayLine[6])):
            MaxVolume = int(arrayLine[6])
            MaxVolumeDate = arrayLine[0]

        if (MinVolume >= int(arrayLine[6])):
            MinVolume = int(arrayLine[6])
            MinVolumeDate = arrayLine[0]

        if (LowestOpen >= float(arrayLine[1])):
            LowestOpen = float(arrayLine[1])
            LowestOpenDate = arrayLine[0]

        if (HighestClose <= float(arrayLine[4])):
            HighestClose = float(arrayLine[4])
            HighestCloseDate = arrayLine[0]

        for i in range(1,13):
            if i==10 or i==11 or i ==12 :
                text = "-" + str(i) +"-"
            else:
                text = "-0" + str(i)  + "-"
            if arrayLine[0].find(text)!= -1:
                HighestmonthAverageList[i-1] = HighestmonthAverageList[i-1] + float(arrayLine[2])
                LowestmonthAverageList[i-1] = LowestmonthAverageList[i-1] + float(arrayLine[3])
                monthAverageListCount[i-1] = monthAverageListCount[i-1] + 1

                listMonthAverageVolume[i-1] = listMonthAverageVolume[i-1] + int(arrayLine[6])
                listMonthAverageCloseValue[i-1] = listMonthAverageCloseValue[i-1] + float(arrayLine[4])
    
    for i in range (len(monthAverageListCount)):
        if monthAverageListCount[i] != 0:
            HighestmonthAverageList[i] = HighestmonthAverageList[i]/monthAverageListCount[i]
            LowestmonthAverageList[i] = LowestmonthAverageList[i]/monthAverageListCount[i]
            listMonthAverageVolume[i] = listMonthAverageVolume[i]/monthAverageListCount[i]
            listMonthAverageCloseValue[i] = listMonthAverageCloseValue[i]/monthAverageListCount[i]

    for po in range(0, len(HighestmonthAverageList)):
        if HighestmonthAverageList[po] == max(HighestmonthAverageList):
            monthAverageMax = po
            monthAverageMaxValue = round(HighestmonthAverageList[po],6)
    
    for po in range(0, len(LowestmonthAverageList)):
        if LowestmonthAverageList[po] == 0:
            LowestmonthAverageList[po] = MAX_DEFAULT
        if LowestmonthAverageList[po] == min(LowestmonthAverageList):
            monthAverageMin = po
            monthAverageMinValue = round(min(LowestmonthAverageList),6)

    volumeAnualAverage = int(sum(volumeAnualAverageList)/len(volumeAnualAverageList)) 

    analysisList.append(MaxVolume) 
    analysisList.append(MaxVolumeDate) 
    analysisList.append(MinVolume) 
    analysisList.append(MinVolumeDate) 
    analysisList.append(LowestOpen) 
    analysisList.append(LowestOpenDate) 
    analysisList.append(HighestClose) 
    analysisList.append(HighestCloseDate) 
    analysisList.append(convertPo2Month(monthAverageMax + 1)) 
    analysisList.append(monthAverageMaxValue)
    analysisList.append(convertPo2Month(monthAverageMin + 1)) 
    analysisList.append(monthAverageMinValue)
    analysisList.append(volumeAnualAverage)
    return analysisList,listMonthAverageVolume,listMonthAverageCloseValue


def DrawVisualise(ay1,ay2):
    xMonth = np.arange(1, 13, 1)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(xMonth, ay1, 'r-')
    ax2.bar(xMonth, ay2)

    ax1.set_xlabel('Apple Stock Price in '+UserYearSelect)
    ax1.set_ylabel('Closed Value ', color='r')
    ax2.set_ylabel('Volume Value', color='b')
    plt.show()


def SaveAnalyseData(inData):
    try:
        with open('result.txt', 'w+') as f:
            for lineD in inData:
                f.writelines(lineD)
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: #handle other exceptions such as attribute errors
        print ("Unexpected error:", sys.exc_info()[0])

    s = int (time.time())
    os.rename('result.txt',"result_"+ str(s)+".txt")



# main program start
listData = OpenInputFile('AAPL_Group.txt')

for lineData in listData:
    arrayLine = lineData.split(',')
    YearData = arrayLine[0]

    if YearData.find("2020-")!= -1:
        listData2020.append(lineData)
    elif YearData.find("2021-")!= -1:
        listData2021.append(lineData)


List2020AnalysisData, listMonthAverageVolume2020,listMonthAverageCloseValue2020 = Analysis (listData2020)
List2021AnalysisData, listMonthAverageVolume2021,listMonthAverageCloseValue2021= Analysis (listData2021)


space = "               "
endline = "\n"
linesData = []
linesData.append("              Apple Stock Analysis 2020 and 2021 \n ")
linesData.append("                          2020                     2021                      Total \n")
linesData.append("Max Volume (Date) \t" + List2020AnalysisData[1] + space + List2021AnalysisData[1]+ space + str(List2020AnalysisData[0]+List2021AnalysisData[0])+endline)
linesData.append("Min Volume (Date) \t" + List2020AnalysisData[3] + space + List2021AnalysisData[3]+ space + str(List2020AnalysisData[2]+List2021AnalysisData[2])+endline)
linesData.append("Lowest Open (Date) \t" + List2020AnalysisData[5] + space + List2021AnalysisData[5]+ space + str(List2020AnalysisData[4]+List2021AnalysisData[4])+endline)
linesData.append("Highest Close (Date) \t" + List2020AnalysisData[7] + space + List2021AnalysisData[7]+ space + str(List2020AnalysisData[6]+List2021AnalysisData[6])+endline)
linesData.append("Highest Monthly \nAverage (Month) \t" + List2020AnalysisData[8] + space + "\t" + List2021AnalysisData[8]+ space + "\t" + str(List2020AnalysisData[9]+List2021AnalysisData[9])+endline)
linesData.append("Lowest Monthly \nAverage (Month) \t" + List2020AnalysisData[10] + space + "\t" + List2021AnalysisData[10]+ space + "\t" + str(round(List2020AnalysisData[11]+List2021AnalysisData[11],6))+endline)
linesData.append("Annual Average \t\t" + str(List2020AnalysisData[12]) + space + str(List2021AnalysisData[12])+ space + str(List2020AnalysisData[12]+List2021AnalysisData[12])+endline)
 
# save final result to txt file
SaveAnalyseData(linesData)

# user select year to show
UserYearSelect = input("Please select year :")
if UserYearSelect == '2020':
    Y_VolumeGr = listMonthAverageVolume2020
    Y_CloseValeGr = listMonthAverageCloseValue2020
elif UserYearSelect == '2021':
    Y_VolumeGr = listMonthAverageVolume2021
    Y_CloseValeGr = listMonthAverageCloseValue2021
else:
    print("Select year again !!")

# draw line for visualization
DrawVisualise(Y_CloseValeGr,Y_VolumeGr)

