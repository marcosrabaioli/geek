from django.db import models
import uuid

# Create your Models here.

class BitcoinQuotation(models.Model):

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    date = models.DateTimeField()
    buy = models.FloatField()
    sell = models.FloatField()
    variation = models.FloatField()