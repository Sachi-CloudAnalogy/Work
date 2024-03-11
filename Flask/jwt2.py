import jwt

token = jwt.encode({"some": "data"}, "secret", algorithm="HS256")
print(token)

data = jwt.decode(token, 'secret', algorithms=["HS256"])
print(data)