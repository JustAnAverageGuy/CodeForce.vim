import requests

HANDLE = "your_handle_here"

html = requests.get(f"http://codeforces.com/api/user.status?handle={HANDLE}&from=1&count=1").json()['result']
print(html[0]['verdict'])
