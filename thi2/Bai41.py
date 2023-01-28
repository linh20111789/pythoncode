def tinh_tien_thanh_toan(sotien,la_khach_vip):
    thanhtoan=0
    if la_khach_vip =='1':
        thanhtoan=float((sotien*90)/100)
    else: thanhtoan=sotien
    return thanhtoan
def LuuFile(danhsachmathang):
    fi = open('danhsach.txt', 'w', encoding= "utf-8")
    for key,value in danhsachmathang.items():
        print(key,value)
        fi.write(key + ": " + str(value) + "\n")
    fi.close()    
tl = 1
danhsachmathang = {}
while (tl == 1):
    tenhang=input('Nhập tên hàng: ')
    dongia=eval(input('Nhập đơn giá: ')) 
    danhsachmathang[tenhang]=dongia
    tl=eval(input("Nhập nữa không? (0: Không/1: Có): "))
    if tl==1:
        continue
    else: break
        
LuuFile(danhsachmathang)  
     