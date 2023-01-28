print(" Nhập số N: ", end="")  
ListN = [int(i)for i in input().split()]
    
print("In ra số chẵn:")    
for i in ListN:
    if i % 2 == 0:
        print(i, end=' ')
    else:
        print("Không tồn tại số chẵn trong danh sách")
        
        
print("\r\nIn ra số chia hết 2 và 3:")    
for i in ListN:
    if i % 2 == 0 and i%3 == 0:
        print(i, end=' ')        
    else:
        print("Không tồn tại số chia hết 2 và 3 trong danh sách")
                
print("\r\nIn ra số âm:")    
for i in ListN:
    if i < 0:
        print(i, end=' ')      
    else:
        print("Không tồn tại số âm trong danh sách")                  
        
print("\r\nTính trung bình cộng:")    
tongDanhSach = sum(ListN)
soPhanTu = len(ListN)
trungBinhCong = tongDanhSach/soPhanTu
print(trungBinhCong, end=' ')         
