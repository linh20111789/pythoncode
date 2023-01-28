StoreManage = {'Quần': 10}
print(StoreManage)
Check = True
while Check == True:
    try:
        keyG= input("Enter goods: ")
        valueG = int(input("Enter numbers of goods: "))

        if keyG in StoreManage:
            print("Existed ")
            up = StoreManage[keyG]= StoreManage.get(keyG) + valueG
            print("up = ",up)

        else:
            print("Not existed")
            StoreManage.update({keyG:valueG})
    except:
        print("input is not correct")

    print(StoreManage)