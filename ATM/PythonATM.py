import random
import sys

class ATM():
    def __init__(self, name, so_tk, namsinh, sdt, so_du = 0):
        self.name_upper = name
        self.so_tk = so_tk
        self.namsinh = namsinh
        self.sdt = sdt
        self.so_du = so_du      

    def nhap():
        name_upper = input("Nhập tên: ")
        so_tk = input("Nhập số tài khoản: ")
        namsinh = input("Nhập năm sinh: ")
        sdt = input("Nhập số điện thoại: ")
        so_du = input("Nhập số dư ban đầu: ")
    def vantin_tk():
        print("\n----------Thông Tin Tài Khoản----------")
        print(f"Chủ tài khoản: {name_upper}")
        print(f"Số tài khoản: {so_tk}")
        print(f"Số dư tài khoản: ",so_du,"\n")
        

    def gui_tien(self, amount):
        self.amount = amount
        self.so_du = self.so_du + self.amount
        print("Số dư tài khoản hiện tại: ", self.so_du)
        print()
 
    def rut_tien(self, amount):
        self.amount = amount
        if self.amount > self.so_du:
            print("Số dư không đủ!")
            print(f"Số dư của bạn chỉ còn {self.so_du}")
            print()
        else:
            self.so_du = self.so_du - self.amount
            print(f"{amount} rút tiền thành công")
            print("Số dư tài khoản hiện tại: ", self.so_du)
            print()
 
    def vantin_tk(self):
        print("Số dư khả dụng: ", self.so_du)
        print()
 
    def giao_dich():
        print("""
         ---------------------------------------------
        | Chào mừng bạn đã đến với ngân hàng StarBank |
         ---------------------------------------------

Bạn có thể chọn một trong các tùy chọn sau để thực hiện giao dịch: 
           
            1. Vấn tin tài khoản
            2. Gửi tiền
            3. Rút tiền
            4. Kết thúc
        
        """)
        
        while True:
            try:
                option = int(input("Chọn 1, 2, 3, 4:"))
            except:
                print("Lỗi: Chỉ chọn 1, 2, 3, 4 \n")
                continue
            else:
                if option == 1:
                    ATM.vantin_tk(amount)
                elif option == 2:
                    amount = int(input("Số tiền bạn muốn gửi: "))
                    ATM.gui_tien(amount)
                elif option == 3:
                    amount = int(input("Số tiền bạn muốn rút: "))
                    ATM.rut_tien(amount)
                elif option == 4:
                    print(f"""
                In hóa đơn..............
          ******************************************
              Giao dịch hiện đã hoàn tất.                         
              Số giao dịch: {random.randint(10000, 1000000)} 
              Chủ tài khoản: {self.name_upper()}                  
              Số tài khoản: {self.so_tk}                
              Số dư khả dụng: {self.so_du}                    
 
     Cảm ơn bạn đã giao dịch tại ngân hàng của chúng tôi
                 Hẹn gặp lại bạn lần sau !!!                
          ******************************************
          """)
                    sys.exit()

class taikhoan(ATM):
    def __init__(self, so_tk, matkhau):  
        super().__init__(self, so_tk)
        self.matkhau = matkhau 
        
    def dangnhap():
        print("Chào mừng bạn đã đến với ngân hàng StarBank")
        print("____________________________________________________\n") 
        print("Đăng nhập tài khoản")
        so_tk = int(input("Số tài khoản: "))
        matkhau = int(input("Mật khẩu: "))
        print("Xin chúc mừng! Tài khoản của bạn được tạo thành công....\n")

    def dangky():
        print("Chào mừng bạn đã đến với ngân hàng StarBank")
        print("____________________________________________________\n") 
        print("Đăng ký tài khoản")
        so_tk = int(input("Số tài khoản: "))
        matkhau = int(input("Mật khẩu (yêu cầu nhập đúng 4 số): "))
        while True:
            matkhau1 = int(input("Yêu cầu nhập lại mật khẩu: "))
            if matkhau == matkhau1:
                print("Đăng ký tài khoản thành công")
                break
            else:
                print("Vui lòng nhập lại")


while True:
    trans = input("Bạn muốn đăng nhập hay đăng kí? 1 là đăng nhập - 2 là đăng ký: ")
    if trans == "1":
        taikhoan.dangnhap()
        menugiaodich = input("Bạn có muốn chuyển tới menu giao dịch không? 1 là có - 2 là không: ")
        if menugiaodich == "1":
            ATM.giao_dich()
        elif menugiaodich == "2":
            break
        else:
            print("Lỗi! Vui lòng chỉ nhập nhập 1 hoặc 2")

    elif trans == "2":
        taikhoan.dangky()
        ATM.nhap()
        menugiaodich = input("Bạn có muốn chuyển tới menu giao dịch không? 1 là có - 2 là không: ")
        if menugiaodich == "1":
            ATM.giao_dich()
        elif menugiaodich == "2":
            break
        else:
            print("Lỗi! Vui lòng chỉ nhập nhập 1 hoặc 2")
    else:
        print("Lỗi!  Chọn '1' là đăng nhập và '2' là đăng ký.\n")