import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from vendor.models import Vendor
from vendor.test_vendor import authenticated_user

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def vendor():
    return Vendor.objects.create(name="Test Vendor", address="Vendor Address", vendor_code="V123", on_time_delivery_rate=95.0, quality_rating_avg=4.0, average_response_time=2.0, fulfillment_rate=90.0)

@pytest.fixture
def purchase_order_data(vendor):
    return {
        'vendor': vendor.id,
        'delivery_date': '2023-12-31T23:59:59Z',
        'items': {'item1': 5, 'item2': 10},
        'quantity': 15,
        'status': PurchaseOrder.PENDING,
        'quality_rating': 4.5,
        'issue_date': '2023-12-01T12:00:00Z',
        'acknowledgement_date': '2023-12-02T12:00:00Z',
    }

@pytest.mark.django_db
def test_purchase_order_list_create_authenticated(api_client, vendor, purchase_order_data, authenticated_user):
    api_client.force_authenticate(user=None)  # Unauthenticate user
    url = reverse('po-list-create')
    response = api_client.post(url, data=purchase_order_data, format='json')

    assert response.status_code == status.HTTP_403_FORBIDDEN

    api_client.force_authenticate(user=authenticated_user)  # Authenticate as a vendor
    response = api_client.post(url, data=purchase_order_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert PurchaseOrder.objects.count() == 1
    assert PurchaseOrder.objects.get().vendor == vendor

# @pytest.mark.django_db
# def test_purchase_order_retrieve_update_destroy_authenticated(api_client, authenticated_user, vendor, purchase_order_data):
#     api_client.force_authenticate(user=authenticated_user)
#     purchase_order_data.pop('vendor')
#     purchase_order = PurchaseOrder.objects.create(vendor=vendor,**purchase_order_data)
#     url = reverse('po-rud', args=[purchase_order.id])

#     # Retrieve
#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK
#     assert response.data['vendor'] == vendor.id

#     # Update
#     updated_data = {
#         'delivery_date': '2023-12-31T23:59:59Z',
#         'status': PurchaseOrder.COMPLETED,
#         'vendor': vendor.id,
#         'items': {'item1': 5, 'item2': 10},
#         'quantity': 15,
#         'quality_rating': 4.5,
#         'issue_date': '2023-12-01T12:00:00Z',
#         'acknowledgement_date': '2023-12-02T12:00:00Z',
    
#     }
#     response = api_client.put(url, data=updated_data, format='json')
#     assert response.status_code == status.HTTP_200_OK
#     assert PurchaseOrder.objects.get().status == PurchaseOrder.COMPLETED
#     # Destroy
#     response = api_client.delete(url)
#     assert response.status_code == status.HTTP_204_NO_CONTENT
#     assert PurchaseOrder.objects.count() == 0

@pytest.mark.django_db
def test_purchase_order_retrieve_update_destroy_unauthenticated(api_client, vendor, purchase_order_data):
    purchase_order_data.pop("vendor")
    purchase_order = PurchaseOrder.objects.create(vendor=vendor,**purchase_order_data)
    url = reverse('po-rud', args=[purchase_order.id])

    # Retrieve
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Update
    updated_data = {'delivery_date': '2023-12-31T23:59:59Z', 'status': PurchaseOrder.COMPLETED}
    response = api_client.put(url, data=updated_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Destroy
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
