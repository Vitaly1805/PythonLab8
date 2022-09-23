import requests

r = requests.get('https://httpbin.org/get', params={'key': 'val'})
print("GET:")
print(r.text)

payload = {'name': 'Vitaly', 'lastname': 'Nosov', 'year_of_birthday': 2000}
r = requests.post('https://httpbin.org/post', data=payload)
print("POST:")
print(r.text)

r = requests.put('https://httpbin.org/put', data={'key': 'value'})
print("PUT:")
print(r.text)


rdd = requests.delete('https://httpbin.org/delete', data ={'key':'value'})
print("DELETE:")
print(rdd.json())


r = requests.head('https://httpbin.org/get')
print("\nHEAD:")
print(r.headers)


r = requests.options('https://httpbin.org/get')
print("\nOPTIONS:")
print(r.headers)
