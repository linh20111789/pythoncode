def tinh_tien_thanh_toan(sotien,la_khach_vip):
    thanhtoan = 0
    if la_khach_vip is "1":
        thanhtoan = float(sotien*0,9)
    else:
        thanhtoan = sotien    
    return thanhtoan
            

print("Nhap ten hang:", end="")
tenhang = input()

print("Nhap don gia:", end="")
dongia = input()

print("khach VIP?(0: khong/1 : co):")
isvip = input()

print("-----HOA DON ------")
print(tenhang, end=":   ")
dongia = "{:,}".format(int(dongia))
print(dongia)
print("Khach hang VIP:", end="")
if isvip is "1":
    print("Co")
else:
    print("khong")

print("Tien thanh toan:  ", end="")    
thanhtoan = tinh_tien_thanh_toan(dongia, isvip)
print(thanhtoan)