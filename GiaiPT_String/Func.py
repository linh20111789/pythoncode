import math  

def convertStr(strings):
    switcher = {
        "một": 1,
        "hai": 2,
        "ba": 3,
        "bốn": 4,
        "năm": 5,
        "sáu": 6,
        "bảy": 7,
        "tám": 8,
        "chín": 9,
    }
 
    return switcher.get(strings, "nothing")




def KiemTraPhuongTrinh(strin):
    checkPT = True
    for i in range(len(strin)):
        print(strin[i])
        if strin[i] == 'bằng'and strnew[i+1] == "không" or strin[i] == '='and strnew[i+1] == "0" :
            checkPT = True
            return checkPT
        else:
            # print("check false")
            checkPT = False

def CheckCongTru(strCT, Bien):
    if strCT == "cộng" or strCT =="+":
        return Bien
    if strCT == "trừ" or strCT =="-":
        return -Bien


def GiaiPhuongTrinh(strin):
    
    if KiemTraPhuongTrinh(strnew)== True:
        for i in range(len(strin)):
            # print("Phương trình OK")
            if strnew[i] == "bình" and strnew[i+1] == "phương":
                GiaTri_A = int(strnew[i-2])
            elif strnew[i]=="x2":
                GiaTri_A = int(strnew[i-1]) 

            if strnew[i] == "x" and strnew[i] != "bình":
                GiaTri_B= CheckCongTru(strnew[i-2], int(strnew[i-1]))    
                
            if strnew[i] == "bằng" and strnew[i+1] == "không" or strin[i] == '='and strnew[i+1] == "0":    
                GiaTri_C= CheckCongTru(strnew[i-2], int(strnew[i-1]))      
        print("A,B,C",GiaTri_A,GiaTri_B,GiaTri_C)
        return GiaTri_A,GiaTri_B,GiaTri_C
    else:
        print("Câu vừa nhập là câu thông thường không chứa phương trình theo yêu cầu")
        return 0,0,0

def CheckCongTru(strCT, Bien):
    if strCT == "cộng" or strCT =="+":
        return Bien
    if strCT == "trừ" or strCT =="-":
        return -Bien

 


# function for finding roots  
def TimNghiem(a, b, c):  
  
    dis_form = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis_form))  
  
  
    if dis_form > 0:  
        print(" Phương trình có 2 nghiệm phân biệt ")  
        print((-b + sqrt_val) / (2 * a))  
        print((-b - sqrt_val) / (2 * a))  
  
    elif dis_form == 0:  
        print(" Phương trình có nghiệm kép")  
        print(-b / (2 * a))  
  
    else:  
        print("Nghiệm phức")  
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val)  


print(" Nhap phuong trinh: ")  
strInput = str(input())

print(strInput)

a = convertStr("một")
print("test" ,a)
strInput = strInput.lower()
print("strInput" ,strInput)
print("strInput" ,type(strInput))
if strInput.find("bình phương") == -1:
    print("Bac 1...")
else :
    print("Bac 2... ")
strnew = strInput.split()

a,b,c =  GiaiPhuongTrinh(strnew) 
TimNghiem(a,b,c)
