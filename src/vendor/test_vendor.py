import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor

@pytest.mark.django_db
def test_vendor_list_create_authenticated(api_client, vendor_data, authenticated_user):
    api_client.force_authenticate(user=authenticated_user)
    url = reverse('vendor-list-create')
    response = api_client.post(url, data=vendor_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert Vendor.objects.count() == 1
    assert Vendor.objects.get().name == vendor_data['name']

@pytest.mark.django_db
def test_vendor_list_create_unauthenticated(api_client, vendor_data, authenticated_user):
    url = reverse('vendor-list-create')
    response = api_client.post(url, data=vendor_data, format='json')

    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_vendor_retrieve_update_destroy_authenticated(api_client, vendor_data, authenticated_user):
    api_client.force_authenticate(user=authenticated_user)
    vendor = Vendor.objects.create(**vendor_data)
    url = reverse('vendor-rud', args=[vendor.id])

    # Retrieve
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == vendor_data['name']

    # Update
    updated_data = {
    'name': 'Updated Vendor Name',
    'address': 'Updated Address',
    'vendor_code': vendor.vendor_code, 
    'on_time_delivery_rate':vendor.on_time_delivery_rate, 
    'quality_rating_avg': vendor.quality_rating_avg, 
    'average_response_time': vendor.average_response_time, 
    'fulfillment_rate': vendor.fulfillment_rate,
}
    response = api_client.put(url, data=updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Vendor.objects.get().name == updated_data['name']
    assert Vendor.objects.get().address == updated_data['address']

    # Destroy
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Vendor.objects.count() == 0

@pytest.mark.django_db
def test_vendor_retrieve_update_destroy_unauthenticated(api_client, vendor_data):
    vendor = Vendor.objects.create(**vendor_data)
    url = reverse('vendor-rud', args=[vendor.id])

    # Retrieve
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Update
    updated_data = {'name': 'Updated Vendor Name', 'address': 'Updated Address'}
    response = api_client.put(url, data=updated_data, format='json')
    assert response.status_code == status.HTTP_403_FORBIDDEN

    # Destroy
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def vendor_data():
    return {
        'name': 'Test Vendor',
        'address': 'Test Address',
        # 'vendor_code': '123',
        'on_time_delivery_rate': 95.5,
        'quality_rating_avg': 4.5,
        'average_response_time': 2.5,
        'fulfillment_rate': 90.0,
    }

@pytest.fixture
def authenticated_user(django_user_model):
    return django_user_model.objects.create(username='testuser', password='testpassword', email="testuser@test.com", is_active=True)
