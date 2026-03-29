from ninja import Router
from .schemas import LoginPayload,RefreshPayload
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from ninja.errors import HttpError

router = Router()

@router.post("/login",auth=None)
def login(request, data: LoginPayload):
    user = authenticate(username=data.username, password=data.password)
    
    if user is not None:
        if user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        else:
            raise HttpError(403, "Requested account is disabled")
    else:
        raise HttpError(401, "Invalid username or password")
    

@router.post("/refresh", auth=None)
def refresh_token(request, data: RefreshPayload):
    try:
        refresh = RefreshToken(data.refresh) # type: ignore
        
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
    except Exception:
        raise HttpError(401, "Invalid or expired refresh token")