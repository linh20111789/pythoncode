import pandas as pd
print("Hello")
df = pd.read_html('https://s.cafef.vn/Lich-su-giao-dich-VHC-6.chn?date=10/06/2022')

new_data = df[3]



print(new_data)

print(type(new_data))

data = list(new_data.columns)

print(data)
# data_top = new_data.head() 
# print(data_top)


data_std = new_data[new_data[2] > 3000]

print(data_std)


# print(new_data[2])





# for i in range(0,1500):
#     print(new_data[2][i])



