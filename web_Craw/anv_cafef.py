import pandas as pd
print("Hello")
df = pd.read_html('https://s.cafef.vn/hose/ANV-cong-ty-co-phan-nam-viet.chn')

print(df[0])
print(type(df))
print(len(df))

# for i in range(len(df)):
#     print("result = {i}\n ",df[i])

print(df[0])
