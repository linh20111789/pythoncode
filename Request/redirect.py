import requests
 
url = 'https://www.facebook.com/'
r = requests.get(url)
 
for redirect in r.history:
    print(redirect.url, redirect.status_code)
print(r.url, r.status_code)


