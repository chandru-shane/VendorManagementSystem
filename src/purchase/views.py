from datetime import datetime
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
# Create your views here.
# 
#     



class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated,]
    filterset_fields = ['vendor']
    filter_backends = [DjangoFilterBackend]

class PurchaseOrderRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated,] 
    lookup_field = "po_number"


class AcknowledgeAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
    
    def post(self, request, po_number, *args, **kwargs):
        po = generics.get_object_or_404(PurchaseOrder, po_number=po_number)
        po.acknowledgement_date = datetime.now()
        po.save()
        return Response({"success":True}, status=status.HTTP_200_OK)
