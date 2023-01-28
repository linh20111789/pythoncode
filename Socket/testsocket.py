
import requests

url = 'http://www.cit.ctu.edu.vn'
r = requests.get(url)
r.text
print(r.text)