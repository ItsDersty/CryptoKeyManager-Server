from ninja import Schema

class LoginPayload(Schema):
    username: str
    password: str