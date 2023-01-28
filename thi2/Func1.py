Checklist = ["GCD", "LCM", "FRAC"]

def UCLN(num1, num2):
    if (num2 == 0):
        return num1
    return UCLN(num2, num1 % num2)

def BCNN(num1, num2):
    return int((num1 * num2) / UCLN(num1, num2))

#partA
checkDK = True
while (checkDK == True):
    print("Nhap dau vao la chuoi:")
    str1 = input()
    if str1 not in Checklist:
        checkDK = True
        print("Nhap lai lan nua:")
    else:
        checkDK = False
        print("checkDK == False")

checkDK = True
while (checkDK == True):
    checkDK = False
    print("Nhap so thu 1:")   
    try:  
        number1 = int(input())
        if isinstance(number1, int) is False:
            checkDK = True
            print("Nhap lai lan nua:")
    except:
        checkDK = True        
        print("Nhap lai lan nua:")

checkDK = True      
while (checkDK == True):
    checkDK = False
    print("Nhap so thu 2:") 
    try:     
        number2 = int(input())
        if isinstance(number2, int) is False:
            checkDK = True
            print("Nhap lai lan nua:")
    except:
        checkDK = True        
        print("Nhap lai lan nua:")      

#partB
if str1 == "GCD":
    print("Uoc chung lon nhat:", UCLN(number1, number2))

elif str1 == "LCM":
    print("Boi chung nho nhat:" , BCNN(number1, number2))

elif str1 == "FRAC":
    print("Rut gon phan so :"+ str(int(number1/UCLN(number1, number2))) + "/" + str(int(number2/UCLN(number1, number2))))        