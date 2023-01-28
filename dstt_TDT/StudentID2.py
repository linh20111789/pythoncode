from re import I
import scipy.io 
import numpy as np


mat = scipy.io.loadmat('data.mat')
# print(mat)
# data = loadmat('data.mat')
# print(data)

# mat2 = np.loadtxt('data.mat')
# print(mat2)
print("----------------transactions--------------------")
transactions = mat['transactions']  # variable in mat file 
print(type(transactions))
print(transactions)
print("----------------transactions ndim--------------------")
print(transactions.ndim)
print("----------------transactions size--------------------")
print(transactions.size)
print("----------------transactions--------------------")
print(transactions.shape)
print("----------------transactions shape[0]--------------------")
print(transactions.shape[0])
print("----------------transactions shape[1]--------------------")
print(transactions.shape[1])
print(len(transactions))
print(transactions[0][0][0])
print(transactions[1][0][0])
print(transactions[2][0][0])
print(transactions[2][0])
print("----------------transactions [2][1]--------------------")
print(transactions[2][1])
print("----------------transactions [2][1] size--------------------")
print(transactions[2][1].size)

print("----------------transactions [8][1] size--------------------")
print(transactions[8][1].size)

print(transactions[2][1][0])
# print(transactions[2])
# print("----------------products--------------------")
# products = mat['products']  # variable in mat file 
# print(products)


# print("----------------history--------------------")
# history = mat['history']  # variable in mat file 
# print(history)
########## Requirements ######
print("req1")
def req1(transactions):    
    newlist = []
    newlistcount = []
    newlistcountmax = []
    newlistcountmin = []
    for i in range(0,transactions.shape[0]):
        # print(transactions[i][1].size)
        for j in range(0,transactions[i][1].size):
            newlist.append(transactions[i][1][j])
        # print(transactions[i])
    print("newlist")
    print(newlist)
    for i in range(len(newlist)-1): 
        newlistcount.append(newlist.count(newlist[i]))

    print("newlistcount")
    print(newlistcount)

    for i in range(len(newlistcount)-1):
        if newlistcount[i] == max(newlistcount):
            newlistcountmax.append(newlist[i])

        if newlistcount[i] == min(newlistcount):
            newlistcountmin.append(newlist[i])

    newlistcountmax=list(set(newlistcountmax))
    newlistcountmin=list(set(newlistcountmin))

    print("newlistcountmax")
    print(newlistcountmax)   

    print("newlistcountmin")
    print(newlistcountmin)  
 
    return newlistcountmax,newlistcountmin
 
def req2(products):
    return None

def req3(transactions, products):
    return None

def req4(transactions, products):
    return None 

def req5(history, k):
    return None

def req6(transactions, history, k):
    return None

def req7(transactions, history):
    return None

def req8(transactions, history, k):
    return None

def req9(transactions, history, products):
    return None

def req10(history, transactions, products, k):
    return None


req1(transactions)