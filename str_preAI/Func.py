

str1 = "Boot time is super fast , around anywhere from 35 seconds to 1 minute ."
str2 = ["Boot time is" , "fast", "P" ]
str3 = "boot time is , fast, P"
print(str1)
print(str2)
print(str2[0])
print(str2[1])

str1new = str1.split()
print("str1new",str1new)

str2new = str2[0].split()
print("str2new",str2new)


print("str3 ",str3)

result = []
result1 = []
result2 = []

print("tesst:")
for idata in str2new:
    
    print("idata = ", idata)
    for i in range(len(str1new)):
        if idata == str1new[i]:
            print("i = ", i)
            result1.append(i)

for idata in str2[1].split():
    
    print("idata = ", idata)
    for i in range(len(str1new)):
        if idata == str1new[i]:
            print("i = ", i)      
            result2.append(i)      

PNN = ''
if str2[2] == "P":
    print("POS")   
    PNN =  'POS'            
elif str2[2] == "N":
    print("NEG")
    PNN = 'NEG'
elif str2[2] == "E":
    print("NEU")   
    PNN  = 'NEU'   

result.append(result1)
result.append(result2)
result.append(PNN)

print("result = ",result)