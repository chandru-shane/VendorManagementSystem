from django.urls import path
from .views import VendorListCreateAPIView, VenderRetrieveUpdateDestoryAPIView
from metrics.views import HistoricalPerformanceRetriveAPIView 



urlpatterns = [
    path("", VendorListCreateAPIView.as_view(), name="vendor-list-create"),
    path("<int:pk>/", VenderRetrieveUpdateDestoryAPIView.as_view(), name="vendor-rud"),
    path("<int:vendor_id>/performance/", HistoricalPerformanceRetriveAPIView.as_view(), name="analytics")
]
