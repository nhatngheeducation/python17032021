
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')
print(r)
print('status =', r.status_code)
if r.status_code == 200: # trả về thành công
    data = r.json() # list
    for item in data:
        print(item["userId"])