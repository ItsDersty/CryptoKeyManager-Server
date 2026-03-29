from ninja import Schema,Field
from datetime import datetime

class VaultEntryOut(Schema):
    id: int
    entry_type: str
    iv: str
    content: dict 
    creation_date: datetime

class NewVaultPayload(Schema):
    entry_type: str=Field(...,max_length=20)
    iv: str=Field(...,min_length=16,max_length=64)
    content: dict