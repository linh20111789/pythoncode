
from array import array
from asyncio.windows_events import NULL
import os, time, sys 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

listData = []
listData2020 = []
listData2021 = []

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
    monthAverageListCount = [0,0,0,0,0,0,0,0,0,0,0,0]
    listMonthAverageVolume = [0,0,0,0,0,0,0,0,0,0,0,0]
    listMonthAverageCloseValue= [0,0,0,0,0,0,0,0,0,0,0,0]

    for lineData in data:
        arrayLine = lineData.split(',')

        for i in range(1,13):
            if i==10 or i==11 or i ==12 :
                text = "-" + str(i) +"-"
            else:
                text = "-0" + str(i)  + "-"
            if arrayLine[0].find(text)!= -1:
                monthAverageListCount[i-1] = monthAverageListCount[i-1] + 1
                listMonthAverageVolume[i-1] = listMonthAverageVolume[i-1] + int(arrayLine[6])
                listMonthAverageCloseValue[i-1] = listMonthAverageCloseValue[i-1] + float(arrayLine[4])
    
    for i in range (len(monthAverageListCount)):
        if monthAverageListCount[i] != 0:
            listMonthAverageVolume[i] = listMonthAverageVolume[i]/monthAverageListCount[i]
            listMonthAverageCloseValue[i] = listMonthAverageCloseValue[i]/monthAverageListCount[i]

    return listMonthAverageVolume,listMonthAverageCloseValue


def DrawVisualise(ay1,ay2):
    xMonth = np.arange(1, 13, 1)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(xMonth, ay1, 'r-')
    ax2.plot(xMonth, ay2, 'g-' )

    ax1.set_xlabel('Apple Stock Price in '+UserYearSelect)
    ax1.set_ylabel('Closed Value ', color='r')
    ax2.set_ylabel('Volume Value', color='b')
   
    plt.show()


# main program start
listData = OpenInputFile('AAPL_Group.txt')

for lineData in listData:
    arrayLine = lineData.split(',')
    YearData = arrayLine[0]

    if YearData.find("2020-")!= -1:
        listData2020.append(lineData)
    elif YearData.find("2021-")!= -1:
        listData2021.append(lineData)


listMonthAverageVolume2020,listMonthAverageCloseValue2020 = Analysis (listData2020)
listMonthAverageVolume2021,listMonthAverageCloseValue2021= Analysis (listData2021)


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

