
def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac
while True:
    try:
        x = convert_to_float(input("x = "))
        print(type(x))
        
        y = convert_to_float(input("y = "))
        
        Zfunc = x*y*(x*x-y*y)/(x*x+y*y)
        print("z = ", Zfunc) 
    except:
        print("type is not correct")   
              
