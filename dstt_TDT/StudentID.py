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
print(transactions.ndim)
print(transactions.size)
print(transactions.shape)
print(transactions.shape[0])
print(transactions.shape[1])
print(len(transactions))
print(transactions[0][0][0])
print(transactions[1][0][0])
print(transactions[2][0][0])
print(transactions[2][0])
print(transactions[2][1])
print(transactions[2][1][0])
print(transactions[2])
# print("----------------products--------------------")
# products = mat['products']  # variable in mat file 
# print(products)


# print("----------------history--------------------")
# history = mat['history']  # variable in mat file 
# print(history)
########## Requirements ######
def req1(transactions):    
    return None
 
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
