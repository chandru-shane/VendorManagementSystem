from django.urls import path
from .views import PurchaseOrderListCreateAPIView, PurchaseOrderRetrieveUpdateDestoryAPIView, AcknowledgeAPIView


urlpatterns = [
    path("", PurchaseOrderListCreateAPIView.as_view(), name="po-list-create"),
    path("<int:po_number>/", PurchaseOrderRetrieveUpdateDestoryAPIView.as_view(), name="po-rud"),
    path("<int:po_number>/acknowledge/", AcknowledgeAPIView.as_view(), name="acknowledge")
]
