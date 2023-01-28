import requests
 
url = 'https://crawler-test.com/'
response = requests.get(url)
 
print('URL: ', response.url)
print('Status code: ', response.status_code)
print('HTTP header: ', response.headers)