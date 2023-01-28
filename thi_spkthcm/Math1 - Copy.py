
checkTF = False

while checkTF == False:
    print(" Enter number n: ")  
    try:
        InputN = int(input())
        listN = []
        print(type(InputN))
        if type(InputN) is int and InputN > 0:
            print("OK")
            checkTF = True
            print("Enter n interger value: ")
            for i in range(0,InputN):
                try:
                    DataIn = int(input(f"number {i} is "))
                    listN.append(DataIn)
                except:
                    print(f"type number {i} is not interger")   
                    checkTF = False       
            print("List", listN) 

            MaxData = max(listN)
            print("Max interger = ", MaxData)
            print("Do you want to continue? y to continue, others key to exit")
            if input() == 'y':
                checkTF = False
            else :
                checkTF = True    
        else:
            print("NOT OK") 
            checkTF = False   
    except:
        print("type is not interger")   
        checkTF = False      