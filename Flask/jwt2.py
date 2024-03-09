import jwt
encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print(encoded)