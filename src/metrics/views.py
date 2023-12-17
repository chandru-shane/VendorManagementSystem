from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer


class HistoricalPerformanceRetriveAPIView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "vendor_id"
    
    