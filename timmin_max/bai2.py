Number_N = int (input())

for i in range(Number_N):
    for j in range(Number_N):        
        if i == j  or i == Number_N -1 -j :
            print('*',end= " ")
        else:    
            print('-',end= " ")
    print('\n')    