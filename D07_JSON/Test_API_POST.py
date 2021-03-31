import requests
employee = {
    "name":"Nhất Nghệ",
    "salary":"123",
    "age":"18"
}

# post_req = requests.post(
#     "http://dummy.restapiexample.com/create",
#     employee
# )
# print(post_req.status_code)
# print(post_req.text)

get_emp = requests.get("http://dummy.restapiexample.com/employees")
print(get_emp.text)