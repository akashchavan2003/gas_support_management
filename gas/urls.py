# gas_utility/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceRequestTypeViewSet, 
    CustomerServiceRequestViewSet, 
    CustomerSupportViewSet,
    CustomerAccountViewSet
)

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'request-types', ServiceRequestTypeViewSet, basename='request-types')
router.register(r'customer/requests', CustomerServiceRequestViewSet, basename='customer-requests')
router.register(r'support/requests', CustomerSupportViewSet, basename='support-requests')
router.register(r'customer-accounts', CustomerAccountViewSet, basename='customer-accounts')

urlpatterns = [
    path('', include(router.urls)),
]