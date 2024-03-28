import jwt

print("something")

token = jwt.encode({"some": "data"}, "djkfhg", algorithm='HS256')

print(token)
