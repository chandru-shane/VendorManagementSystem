import pytest

from datetime import datetime
from dateutil import parser

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import HistoricalPerformance
from purchase.models import PurchaseOrder
from vendor.models import Vendor
from vendor.test_vendor import authenticated_user
from purchase.test_purchase import vendor


# @pytest.mark.django_db
# def test_historical_performance_retrieve_authenticated(api_client, historical_performance_data,purchase_order_data, authenticated_user):
#     api_client.force_authenticate(user=authenticated_user)
#     [PurchaseOrder.objects.create(**po_data) for po_data in purchase_order_data]
#     historical_performance = HistoricalPerformance.objects.first()
#     url = reverse('analytics', args=[historical_performance.id])

#     response = api_client.get(url)

#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['vendor'] == historical_performance_data['vendor'].id
#     assert response.data['on_time_delivery_rate'] == 0
#     assert response.data['quality_rating_avg'] == 0
#     assert response.data['average_response_time'] == 0
#     assert response.data['fulfillment_rate'] == 0
#     # assert response.data['date'] == 

@pytest.mark.django_db
def test_update_performance_signal(db, purchase_order_data, vendor_data):
    vendor = Vendor.objects.create(**vendor_data)
    [PurchaseOrder.objects.create(**po_data) for po_data in purchase_order_data]

    historical_performance,_ = HistoricalPerformance.objects.get_or_create(vendor=vendor)
    
    assert historical_performance.on_time_delivery_rate == 0
    assert historical_performance.quality_rating_avg == 0
    assert historical_performance.average_response_time == None
    assert historical_performance.fulfillment_rate == 0
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def historical_performance_data(vendor):
    return {
        'vendor': vendor,
        'date': datetime.now(),
    }

@pytest.fixture
def purchase_order_data(vendor):
    return [
        {
            "vendor":vendor,
            "order_date":parser.parse("2023-12-01 00:00:00"),
            "delivery_date":parser.parse("2023-12-10 00:00:00"),
            "acknowledgement_date":parser.parse("2023-12-01 01:00:00"),
            "status":"PurchaseOrder",
            "items":{},
            "quantity":1,
            "issue_date":parser.parse("2023-12-01 00:00:00"),
            "status":"Pending"
        }
    ]

@pytest.fixture
def vendor_data():
    return {
        'name': 'Test Vendor',
        'address': 'Test Address',
        'vendor_code': '123',
        'on_time_delivery_rate': 95.5,
        'quality_rating_avg': 4.5,
        'average_response_time': 2.5,
        'fulfillment_rate': 90.0,
    }
