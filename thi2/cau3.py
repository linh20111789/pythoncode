def tinh_tien_thanh_toan(sotien,la_khach_vip):
    thanhtoan = 0
    if la_khach_vip is "1":
        thanhtoan = float(sotien*0,9)
    else:
        thanhtoan = sotien    
    return thanhtoan
            
checkDK = True
danhsachmathang = {}
while (checkDK == True):
    print("Nhap ten hang:", end="")
    tenhang = input()

    print("Nhap don gia:", end="")
    dongia = input()
    
    danhsachmathang[tenhang] = dongia
    print(danhsachmathang)
        
    print("Nhap nua khong?(0/1):")
    nhapnua = input()
    if nhapnua == "1":
        checkDK = True
        print("Nhap lai lan nua:")
    else:
        checkDK = False
        tongtien = 0
        print("khach VIP?(0: khong/1 : co):")
        isvip = input()
        print("-----HOA DON ------")
        for ihang in danhsachmathang:
            print(ihang, end=":   ")
            print(danhsachmathang[ihang])
            tongtien = tongtien + int(danhsachmathang[ihang])
        print("--------------")  
        print("Tong", end=":   ")
        tongtien = "{:,}".format(int(tongtien)) 
        print(tongtien)
        print("Khach hang VIP:", end="")
        if isvip is "1":
            print("Co")
            print("Tien thanh toan:  ", end="")  
            thanhtoan = tinh_tien_thanh_toan(tongtien, isvip)
            print(thanhtoan) 
        else:
            print("khong")
            print("Tien thanh toan:  ", end="") 
            print(tongtien) 
         
        