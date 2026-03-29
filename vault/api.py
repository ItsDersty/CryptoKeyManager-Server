from ninja import Router
from typing import List
from .schemas import VaultEntryOut,NewVaultPayload
from ninja.errors import HttpError

router = Router()

@router.get("/get-entries",response=List[VaultEntryOut])
def get_entries(request):
    return request.auth.vault_entries.all()

@router.post("add-entry",response=VaultEntryOut)
def add_entry(request, data:NewVaultPayload):
    user = request.auth
    item = user.vault_entries.create(**data.dict())
    return item

@router.delete("delete-entry",response={204: None})
def delete_entry(request,id:int):
    user = request.auth
    item = user.vault_entries.all().filter(id=id)

    if item:
        item.delete()
        return 204,None
    else:
        raise HttpError(404,"Entry not found")