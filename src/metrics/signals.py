from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import ExpressionWrapper, F, fields
from django.db.models import F, Q, Count, Avg
from purchase.models import PurchaseOrder
from metrics.models import HistoricalPerformance


@receiver(post_save, sender=PurchaseOrder, dispatch_uid="update_perfomance_analytics")
def update_stock(sender, instance, created, **kwargs):
    
    query = PurchaseOrder.objects.filter(vendor=instance.vendor).annotate(
        response_time = ExpressionWrapper(
        F("acknowledgement_date") - F("issue_date"),
    output_field=fields.DurationField(),
),
    
).aggregate(
        on_time=Count("id", filter=Q(deliveried_at__lte=F("delivery_date")), distinct=True),
        completed_count = Count("id", filter=Q(status=PurchaseOrder.COMPLETED), distinct=True),
        total=Count("id", distinct=True),
        quality_rating_avg = Avg("quality_rating",default=0),
        average_response_time=Avg(F"response_time"),
    )

    fulfillment_rate = query["completed_count"]/query["total"] if query["total"] > 0 else 0
    on_time_delivery_rate = query["on_time"]/query["total"] if query["total"] > 0 else 0
    query["on_time_delivery_rate"] = on_time_delivery_rate
    query["fulfillment_rate"] = fulfillment_rate

    hp,_ = HistoricalPerformance.objects.get_or_create(vendor=instance.vendor)
    hp.on_time_delivery_rate = query["on_time_delivery_rate"]
    hp.quality_rating_avg = query["quality_rating_avg"]
    hp.average_response_time = query["average_response_time"]
    hp.fulfillment_rate = query["fulfillment_rate"]
    hp.date = datetime.now()
    hp.save()
