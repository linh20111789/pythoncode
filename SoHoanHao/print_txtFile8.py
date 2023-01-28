

def kiemtraHoanThien(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False



try:
    FileR = open("input.txt", 'r').readlines()
    for n in FileR:
        line = n.strip()
        
        print(type(line))
        for idx, a in enumerate(line):
            print(idx, a)
  
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
