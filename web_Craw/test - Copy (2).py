import pandas as pd
print("Hello")
df = pd.read_html('https://s.cafef.vn/Lich-su-giao-dich-VHC-6.chn#data')

new_data = df[3]



print(new_data)

print(type(new_data))



data_top = new_data.head() 
print(data_top)


# data_std = new_data[new_data['2'] > 4000]

# print(data_std)


print(new_data[2])





# for i in range(0,1500):
#     print(new_data[2][i])



