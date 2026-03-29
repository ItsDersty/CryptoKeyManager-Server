from ninja.security import HttpBearer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model

User=get_user_model()

class JWTAuth(HttpBearer):
    """
    JWT authentification instead of django's default
    We will have a desktop/mobile app, not a web site
    """
    def authenticate(self, request, token):
        try:
            access_token = AccessToken(token) # type: ignore
            user_id = access_token['user_id']
            return User.objects.get(id=user_id)
        except Exception:
            return None