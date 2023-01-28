


import shutil
import os
for i in range(1,100):
    print(i)
    name ="out/"+ "-" + str(i).zfill(3)+".png"
    print(name)
    shutil.copy("image/-000.png",name)
   
ORIGIN_PATH = "out/"
CHANGED_PATH = "change/"
    
list = []
for i in range(1,100):
    print(i)
    name = ORIGIN_PATH + "-" + str(i).zfill(3)+".png"
    print(name)
    number = str(i).zfill(3)
    print((number))
    list.append(name)
    if (int(number)%8 == 0):
        list.append(ORIGIN_PATH + "+" + str(int(number)-7).zfill(3)+".png")
        shutil.copy(ORIGIN_PATH + "-" + str(int(number)-7).zfill(3)+".png",ORIGIN_PATH + "+" + str(int(number)-7).zfill(3)+".png")
print("------------------")      
print(list)         
for i in list:
    print(i)
    newname = list.index(i)
    newname = CHANGED_PATH + str(newname) +".png"
    print(newname)
    os.rename(i, newname)
    
    