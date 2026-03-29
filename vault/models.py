from django.db import models
from django.conf import settings

class VaultEntry(models.Model):
    """
    Class of vault entry elements (passwords, tokens, notes, etc.)
    Class can contain any allowed type of vault entry
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="vault_entries")
    entry_type = models.CharField(max_length=32, db_index=True)
    iv=models.CharField(max_length=64)
    content = models.JSONField()

    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entry_type} of user {self.user.username}"