from ninja import Schema
from datetime import datetime

class VaultEntryOut(Schema):
    id: int
    entry_type: str
    iv: str
    content: dict 
    creation_date: datetime