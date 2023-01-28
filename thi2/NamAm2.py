
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]

def Namam(namduongdich):
    tinh_can = namduongdich % 10
    tinh_chi = namduongdich % 12
    nam_am = can[tinh_can] + " " + chi[tinh_chi]
    print(nam_am)
    return str(nam_am)

def LuuFile():
    fi = open('ketqua.txt', 'w', encoding= "utf-8")
    namsinhamlich = int(input("Nhap vao nam sinh: "))
    fi.write('Nam sinh am lich cua nam ' + str(namsinhamlich) + ' la: ' + Namam(namsinhamlich))
    fi.write('\n')
    namhientaiamlich = int(input("Nhap vao nam hien tai: "))
    fi.write('Nam hien tai am lich cua nam ' + str(namhientaiamlich) + ' la: ' + Namam(namhientaiamlich))
    fi.write('\n')
    fi.close()

Namam(2000)
LuuFile()

