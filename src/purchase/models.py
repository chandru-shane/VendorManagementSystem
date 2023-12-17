from uuid import uuid4

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from vendor.models import Vendor
# Create your models here.



class PurchaseOrder(models.Model):
    
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    
    STATUS_CHOICES = (
        (PENDING, "Pending"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled"),
    )

    po_number = models.CharField(max_length=36, unique=True, default=uuid4)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=64,choices=STATUS_CHOICES, default=PENDING)
    quality_rating = models.FloatField(null=True,validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True)
    deliveried_at = models.DateTimeField(null=True)


