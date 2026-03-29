from ninja import NinjaAPI, Schema
from vault.api import router as vault_router
from users.api import router as users_router
from users.auth import JWTAuth

api = NinjaAPI(
    title="CryptKey API",
    version="v1",
    description="CryptKey",
    auth=JWTAuth(),
)

api.add_router("/vault", vault_router)
api.add_router("/users", users_router)