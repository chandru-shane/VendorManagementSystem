from django.db import models
from vendor.models import Vendor
# Create your models here.


class HistoricalPerformance(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.DurationField(null=True)
    fulfillment_rate = models.FloatField(default=0)


