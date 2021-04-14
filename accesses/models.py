from django.db import models


class DoorUseLog(models.Model):
    user = models.ForeignKey('accounts.user', on_delete=models.CASCADE)
    generation = models.ForeignKey('accounts.generation', on_delete=models.CASCADE)
    create_at = models.DateTimeField()