# gas_utility/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ServiceRequest, ServiceRequestType, CustomerAccount
from .serializers import (
    ServiceRequestSerializer, 
    ServiceRequestTypeSerializer, 
    CustomerAccountSerializer,
    CustomerServiceRequestSerializer
)

class ServiceRequestTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing service request types"""
    queryset = ServiceRequestType.objects.all()
    serializer_class = ServiceRequestTypeSerializer

class CustomerServiceRequestViewSet(viewsets.ViewSet):
    """ViewSet for customer-specific service request operations"""
    
    def create(self, request):
        """Endpoint for customers to submit new service requests"""
        serializer = CustomerServiceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        """Endpoint to list service requests by customer email"""
        email = request.query_params.get('email', None)
        if not email:
            return Response(
                {"error": "Email parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        requests = ServiceRequest.objects.filter(customer_email=email)
        serializer = ServiceRequestSerializer(requests, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def track_request(self, request):
        """Specific endpoint to track a single request by request ID and email"""
        request_id = request.query_params.get('request_id', None)
        email = request.query_params.get('email', None)
        
        if not (request_id and email):
            return Response(
                {"error": "Both request_id and email are required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            request_obj = ServiceRequest.objects.get(
                id=request_id, 
                customer_email=email
            )
            serializer = ServiceRequestSerializer(request_obj)
            return Response(serializer.data)
        except ServiceRequest.DoesNotExist:
            return Response(
                {"error": "Request not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

class CustomerSupportViewSet(viewsets.ModelViewSet):
    """ViewSet for customer support representatives"""
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    
    def get_queryset(self):
        """Optionally filter requests by status"""
        status_filter = self.request.query_params.get('status', None)
        if status_filter:
            return self.queryset.filter(status=status_filter.upper())
        return self.queryset
    
    @action(detail=True, methods=['PATCH'])
    def update_status(self, request, pk=None):
        """Endpoint to update request status and add support notes"""
        try:
            service_request = self.get_object()
            
            # Update status if provided
            new_status = request.data.get('status', None)
            if new_status:
                service_request.status = new_status
                if new_status == 'RESOLVED':
                    service_request.mark_as_resolved()
            
            # Update support notes if provided
            support_notes = request.data.get('support_notes', None)
            if support_notes:
                service_request.support_notes = support_notes
            
            service_request.save()
            
            serializer = self.get_serializer(service_request)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class CustomerAccountViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for customer account information"""
    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountSerializer
    
    def get_queryset(self):
        """Allow filtering by email"""
        email = self.request.query_params.get('email', None)
        if email:
            return self.queryset.filter(email=email)
        return self.queryset