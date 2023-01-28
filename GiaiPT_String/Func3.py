import math  

def CommonGUI():
    print("TRƯỜNG ĐẠI HỌC BÌNH DƯƠNG")
    print("KHOA CNTT, ROBOT VÀ TTNT")

    print("             BÀI TẬP LỚN CUỐI KÌ")

    print("TRƯỜNG ĐẠI HỌC BÌNH DƯƠNG")

    print("TRƯỜNG ĐẠI HỌC BÌNH DƯƠNG")
    print("TRƯỜNG ĐẠI HỌC BÌNH DƯƠNG")
    print("TRƯỜNG ĐẠI HỌC BÌNH DƯƠNG")
    print("TRƯỜNG ĐẠI HỌC BÌNH DƯƠNG")


def convertStr(strings):
    if strings == "một":
        return 1
    elif strings == "hai":
        return 2
    elif strings == "ba":
        return 3 
    elif strings == "bốn":
        return 4
    elif strings == "năm":
        return 5
    elif strings == "sáu":
        return 6 
    elif strings == "bảy":
        return 7 
    elif strings == "tám":
        return 8
    elif strings == "chín":
        return 9 
    elif strings == "bằng":
        return "="
    else:
        return strings
 

def KiemTraPhuongTrinh(strin):
    checkPT = True
    for i in range(len(strin)):
        print(strin[i])
        if (strin[i] == 'bằng' or strin[i] == '=') and (strnew[i+1] == "không" or strnew[i+1] == '0') :
            checkPT = True
            return checkPT
        else:
            checkPT = False

def CheckCongTru(strCT, Bien):
    if strCT == "cộng" or strCT =="+":
        return Bien
    if strCT == "trừ" or strCT =="-":
        return -Bien


def GiaiPhuongTrinhBac2(strin):
    for i in range(len(strin)):
        # print("Phương trình OK")
        if strin[i] == "bình" and strin[i+1] == "phương":
            GiaTri_A = int(strin[i-2])
        elif strin[i]=="x2":
            GiaTri_A = int(strin[i-1]) 

        if strin[i] == "x" and strin[i] != "bình":
            GiaTri_B= CheckCongTru(strin[i-2], int(strin[i-1]))    
            
        if (strin[i] == "bằng" or strin[i] == '=') and (strin[i+1] == "không" or strin[i+1] == '0'):    
            GiaTri_C= CheckCongTru(strin[i-2], int(strin[i-1]))      
    # print("A,B,C",GiaTri_A,GiaTri_B,GiaTri_C)
    return GiaTri_A,GiaTri_B,GiaTri_C


def GiaiPhuongTrinhBac1(strin):
    for i in range(len(strin)):
        print(strin[i])
        if strin[i] == "x":
            GiaTri_A= int(strin[i-1])  
            
        if (strin[i] == "bằng" or strin[i] == '=') and (strin[i+1] == "không" or strin[i+1] == "0"):    
            GiaTri_B= CheckCongTru(strin[i-2], int(strin[i-1])) 

    if GiaTri_A == 0:
        if GiaTri_B == 0:
            print("Vô số nghiệm")
        else:
            print("Vô nghiệm")
    else:
        print("Nghiệm là ", -GiaTri_B/GiaTri_A)


def KiemTraBac(strin):

    if strin.find("bằng không") != -1 or strin.find("= 0") != -1 or strin.find("= không") != -1 or strin.find("bằng 0") != -1:
        if strin.find("bình phương") != -1:
            return 2
        else :
            return 1 
    else:
        print("Câu vừa nhập là câu thông thường không chứa phương trình theo yêu cầu")
        return 0

# function for finding roots  
def TimNghiemBac2(a, b, c):  
  
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


CommonGUI()

print(" Nhập phương trình: ")  
strInput = str(input())

strInput = strInput.lower()

strnew = strInput.split()

str_Digital = []

for i in range(len(strnew)):
    str_Digital.append(convertStr(strnew[i])) 

LoaiBac = KiemTraBac(strInput)
if (LoaiBac == 2):
    print("PTB2")
    a,b,c = GiaiPhuongTrinhBac2(str_Digital)
    TimNghiemBac2(a,b,c)
elif (LoaiBac == 1):
    print("PTB1")
    GiaiPhuongTrinhBac1(str_Digital)
else:
    pass



