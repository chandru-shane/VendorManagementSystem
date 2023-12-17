from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Vendor
from .serializers import VendorSerializer

# Create your views here.


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated,]

    


class VenderRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated,] 
