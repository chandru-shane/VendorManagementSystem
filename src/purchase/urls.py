from django.urls import path
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestoryAPIView


urlpatterns = [
    path("", PurchaseOrderListCreateAPIView.as_view(), name="po-list-create"),
    path("<int:po_number>/", PurchaseOrderRetrieveUpdateDestoryAPIView.as_view(), name="po-rud"),
    # path("{po_id}/acknowledge/")
]
