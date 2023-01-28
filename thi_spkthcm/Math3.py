# Lap trinh ung dung trong ki thuat – Dai Hoc Su Pham Ki Thuat Thanh Pho Ho Chi Minh
def split(word):
    listL = []
    for char in word:
        print(char)
        if char is not ' ':
            listL.append(char)
    return listL

strInput = input(" Enter sentence: ").lower()
print(strInput)
listStr = split(strInput)
print(listStr)
Max = str(max(listStr,key=listStr.count))
print("The letters (case-insensitive) that appears the most:", Max)
for i in listStr:
    if i == Max:
        listStr.remove(i)
print(listStr)
Max2 = max(listStr,key=listStr.count)
print("The letters (case-insensitive) that appears the second-most :", Max2)




