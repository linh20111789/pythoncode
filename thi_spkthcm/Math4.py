# import numpy as np
# from matplotlib import pyplot as plt

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

# def y1(x):
#     #2x^5  + 10x^4  - 7x^3  - 200x^2  - 200x + 200
#     y1 = 2*x**5 + 10*x**4  - 7*x**3  - 200*x**2  - 200*x + 200
#     return y1

# def y2(x):
#     #20x^4  - 5x^3  - 150x^2  - 140x + 100
#     y1 = 20*x**4  - 5*x**3  - 150*x**2  - 140*x + 100
#     return y1

# x = np.linspace(-10, 10, 100)

# plt.plot(x, y1(x), color='red')

# plt.show()

# import math as m
# import matplotlib.pyplot as plt
# import numpy as np

# def y1(x):
#     #2x^5  + 10x^4  - 7x^3  - 200x^2  - 200x + 200
#     y1 = 2*x**5 + 10*x**4  - 7*x**3  - 200*x**2  - 200*x + 200
#     return y1

# def y2(x):
#     #20x^4  - 5x^3  - 150x^2  - 140x + 100
#     y1 = 20*x**4  - 5*x**3  - 150*x**2  - 140*x + 100
#     return y1

# x = np.linspace( -2,3, 100)
# fd = y1(x)
# be = y2(x)

# plt.figure()
# plt.subplots(x, fd, label='5th degree polinomial')
# plt.subplots(x, be, label ='4th degree polinomial')
# plt.legend(loc='best')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# plt.figure(figsize=(6, 4))

# fig, (ax1, ax2)  = plt.subplots(1, 2,
#                                 sharey='row')

# ax1.text(0.5, 0.5, 
#               "left",
#               color="green",
#               fontsize=18, 
#               ha='center')

# ax2.text(0.5, 0.5, 
#               "right",
#               color="green",
#               fontsize=18, 
#               ha='center')

# x = np.linspace( -2,3, 100)
# def y1(x):
#     #2x^5  + 10x^4  - 7x^3  - 200x^2  - 200x + 200
#     y1 = 2*x**5 + 10*x**4  - 7*x**3  - 200*x**2  - 200*x + 200
#     return y1

# def y2(x):
#     #20x^4  - 5x^3  - 150x^2  - 140x + 100
#     y1 = 20*x**4  - 5*x**3  - 150*x**2  - 140*x + 100
#     return y1

# f, (ax1, ax2) = plt.subplots(1, 2,  sharey=True)
# ax1.plot(x, y1(x))
# ax1.set_title('Sharing Y axis')
# ax2.plot(x, y2(x)) 
# plt.show()    

import matplotlib.pyplot as plt
import numpy as np

def y1(x):
    #2x^5  + 10x^4  - 7x^3  - 200x^2  - 200x + 200
    y = 2*x**5 + 10*x**4  - 7*x**3  - 200*x**2  - 200*x + 200
    return y

def y2(x):
    #20x^4  - 5x^3  - 150x^2  - 140x + 100
    y = 20*x**4  - 5*x**3  - 150*x**2  - 140*x + 100
    return y

#plot 1:
x = np.linspace(-5, 5, 200)
# x = np.array([-4, 3, -2, -1, 0, 1, 2, 3, 4])

plt.subplot(1, 2, 1,label='5th DP')
plt.plot(x,y1(x))
plt.title("5th degree polinomial")

plt.subplot(1, 2, 2, label='4th DP')
plt.plot(x,y2(x))
plt.title("4th degree polinomial")

plt.show()