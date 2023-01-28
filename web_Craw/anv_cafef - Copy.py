
import requests
from bs4 import BeautifulSoup
 
url = "https://vnexpress.net/giao-duc"
 
# Gửi 1 request đến url phía trên và nhận lại source page của nó
r = requests.get(url)
 
print(r.status_code) # 200 là thành công
 
# In thử page source ra coi sao, mình in thử 1000 ký tự đầu tiên thôi
# Bạn có thể thử so sánh với source mà bạn thấy trên trình duyệt
# print(r.content[:1000])
 
 
# Làm đẹp source 
# Mình dùng lxml parser cho nhanh, 
# Ngoài ra có html.parser, lxml-xml, html5lib (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
soup = BeautifulSoup(r.content, 'lxml')
 
print("============TITLE=============")
# Lấy thẻ tiêu đề bài báo
print(soup)
# Lấy nội dung tiêu đề
print(soup.title.text)

for title in soup.find_all('title'):
    print(title.get_text())
 