import requests
 
payload = {
    'name':'Jean-Christophe',
    'last_name':'Chouinard'
    }
 
response = requests.post('https://www.jcchouinard.com/' , data = payload)
 
print(response.content)
print(response.links)
print(response.cookies)



