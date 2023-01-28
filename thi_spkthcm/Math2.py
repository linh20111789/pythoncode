
try:
    listDiv4 = []
    SumEven = 0
    SumOdd = 0
    InputN = int(input(" Enter n: "))
    print("List of integers from 1 to n= ")
    for i in range(1,InputN+1):
        print(" ",i, end="")
        if i%2 == 0:
            SumEven = SumEven + i
        else:
            SumOdd = SumOdd + i
        if i%4 == 0:
            listDiv4.append(i)
    print("\nSum even = ", SumEven)
    print("Sum odd = ", SumOdd) 
    print("List of numbers divisible by 4= ")
    for va in listDiv4:
        print(" ",va, end="")  
    print()       
except:
    print("input is not correct")