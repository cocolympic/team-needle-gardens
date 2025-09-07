import http.client

# 接続先
conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

# GETリクエストを送る
conn.request("GET", "/posts/1")

# レスポンスを受け取る
response = conn.getresponse()

print("Status:", response.status)
print("Reason:", response.reason)
print("Body:", response.read().decode())

# 接続を閉じる
conn.close()
