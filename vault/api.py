from ninja import Router
from typing import List
from .schemas import VaultEntryOut

router = Router()

@router.get("/get-entries",response=List[VaultEntryOut])
def list_items(request):
    return request.auth.vault_entries.all()