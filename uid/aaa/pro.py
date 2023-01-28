from array import array
import os, time, sys 
listData = []

def OpenResultFile(filename):
    ld = []
    re = []
    try:
        FileR = open(filename, 'r').readlines()
        for n in FileR:
            line = n.split(":")[0]
            ld.append(line)
            re.append(n)
        return ld,re    
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: 
        print ("Unexpected error:", sys.exc_info()[0])


def OpenInputFile(filename,re):
    result1 = []
    try:
        FileR = open(filename, 'r').readlines()
        for n in FileR:
            for r in re:
                if n.find(r.split(":")[0]) != -1:
                    print("found")
                    result1.append(r)
        return result1    
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except: 
        print ("Unexpected error:", sys.exc_info()[0])

result,re = OpenResultFile('re.txt')
listData1 = OpenInputFile('1.txt',re)
listData1 = list(dict.fromkeys(listData1))
with open("re_same.txt", "w+") as output:
    for item in listData1:
        output.writelines(item)



