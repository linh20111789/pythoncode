def dem_so_tu(chuoi):
    newstr = []
    strnew = chuoi.split()
    for substr in strnew:
        if substr.find("a") != -1:
            newstr.append(substr)
            
    return newstr
            

print("Nhap dau vao la chuoi:")
str1 = input()

result = dem_so_tu(str1)

print( result)