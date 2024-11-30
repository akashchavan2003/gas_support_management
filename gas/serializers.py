# gas_utility/serializers.py
from rest_framework import serializers
from .models import ServiceRequest, ServiceRequestType, CustomerAccount

class ServiceRequestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequestType
        fields = ['id', 'name', 'description']

class ServiceRequestSerializer(serializers.ModelSerializer):
    """Serializer for Service Requests"""
    request_type_details = ServiceRequestTypeSerializer(source='request_type', read_only=True)
    
    class Meta:
        model = ServiceRequest
        fields = [
            'id', 
            'customer_name', 
            'customer_email', 
            'customer_phone', 
            'request_type', 
            'request_type_details',
            'description', 
            'attachment', 
            'status', 
            'submitted_at', 
            'resolved_at',
            'support_notes'
        ]
        read_only_fields = ['id', 'status', 'submitted_at', 'resolved_at']

class CustomerAccountSerializer(serializers.ModelSerializer):
    """Serializer for Customer Accounts"""
    class Meta:
        model = CustomerAccount
        fields = [
            'id', 
            'name', 
            'email', 
            'phone_number', 
            'address', 
            'account_number'
        ]

class CustomerServiceRequestSerializer(serializers.ModelSerializer):
    """Simplified serializer for customers to submit requests"""
    class Meta:
        model = ServiceRequest
        fields = [
            'customer_name', 
            'customer_email', 
            'customer_phone', 
            'request_type', 
            'description', 
            'attachment'
        ]