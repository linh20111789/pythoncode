print(" Nhập string: ")  
# i love you i . i love 
strInput = str(input())

strInputList =  strInput.split()
print(strInputList)
mylist = list(dict.fromkeys(strInputList))

try:
    mylist.remove('.')
    mylist.remove(',')
except ValueError:
    pass
print(mylist)
for i in mylist:
    count = strInputList.count(i)
    print(i+ ":" + str(count))