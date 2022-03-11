from django.db import models


class Count(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
