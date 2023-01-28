from re import I
import scipy.io 
import numpy as np


mat = scipy.io.loadmat('data.mat')

transactions = mat['transactions']  # variable in mat file 

print("----------------products--------------------")
products = mat['products']  # variable in mat file 
print(products)

print("----------------products ndim--------------------")
print(products.ndim)
print("----------------products size--------------------")
print(products.size)
print("----------------products--------------------")
print(products.shape)
print("----------------products shape[0]--------------------")
print(products.shape[0])
print("----------------products shape[1]--------------------")
print(products.shape[1])

print("----------------products [x][2]--------------------")
print(str(products[0][0]))
print(products[0][2])
print(products[1][2])
print(products[2][2])


# print("----------------history--------------------")
# history = mat['history']  # variable in mat file 
# print(history)
########## Requirements ######

def req1(transactions):    
    newlist = []
    newlistcount = []
    newlistcountmax = []
    newlistcountmin = []
    for i in range(0,transactions.shape[0]):
        for j in range(0,transactions[i][1].size):
            newlist.append(transactions[i][1][j])
    for i in range(len(newlist)-1): 
        newlistcount.append(newlist.count(newlist[i]))

    for i in range(len(newlistcount)-1):
        if newlistcount[i] == max(newlistcount):
            newlistcountmax.append(newlist[i])

        if newlistcount[i] == min(newlistcount):
            newlistcountmin.append(newlist[i])

    newlistcountmax=list(set(newlistcountmax))
    newlistcountmin=list(set(newlistcountmin))

    return newlistcountmax,newlistcountmin
 
def req2(products):
    inventlist = []
    inventcountmax = []
    inventcountmin = []
    for i in range(0,products.shape[0]):
        for j in range(0,products.shape[1]):
            print(products[i][j])

    for i in range(0,products.shape[0]):
        inventlist.append(int(products[i][2])) 

    print("inventlist")
    print(inventlist)  

    print("inventcountmax")
    print(max(inventlist)) 
    print("inventcountmin")
    print(min(inventlist)) 

    for i in range(len(inventlist)-1):
        if int(products[i][2]) == max(inventlist):
            inventcountmax.append(products[i][0])

        if int(products[i][2]) == min(inventlist):
            inventcountmin.append(products[i][0])

    print("inventcountmax")
    print(inventcountmax) 
    print("inventcountmin")
    print(inventcountmin) 
    return inventcountmax,inventcountmin

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
req2(products)