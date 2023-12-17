from django.db import models
from uuid import uuid4

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=1024) 
    address = models.TextField()
    vendor_code = models.CharField(max_length=36, unique=True,default=uuid4)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()