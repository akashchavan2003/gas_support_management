from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model for system users.
    """
    pass


class ServiceRequestType(models.Model):
    """
    Predefined types of service requests.
    Examples: Installation, Repair, Maintenance.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ServiceRequest(models.Model):
    """
    Model to represent customer service requests.
    Includes customer details, request type, status, and timestamps.
    """
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CANCELLED', 'Cancelled')
    ]

    # Customer details
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)

    # Type of service request (linked to predefined types)
    request_type = models.ForeignKey(ServiceRequestType, on_delete=models.SET_NULL, null=True)

    # Request details and attachments
    description = models.TextField()
    attachment = models.FileField(upload_to='service_request_attachments/', blank=True, null=True)

    # Status and timestamps
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    # Notes by support representatives
    support_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Service Request #{self.id} - {self.customer_name}"

    def mark_as_resolved(self):
        """
        Method to mark the request as resolved.
        Updates status and sets resolved_at timestamp.
        """
        self.status = 'RESOLVED'
        self.resolved_at = timezone.now()
        self.save()


class CustomerAccount(models.Model):
    """
    Model to store customer account information.
    Includes personal details, contact information, and account details.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    account_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} - {self.account_number}"
