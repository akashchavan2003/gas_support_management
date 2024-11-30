from django.test import TestCase

# Create your tests here.
# test_gas_utility.py
import requests
import json

# Base URL for your Django application
BASE_URL = 'http://localhost:8000/api/'

def create_sample_data():
    """
    Create sample data for testing the gas utility application
    """
    # Create Sample Request Types
    request_types_data = [
        {"name": "Meter Reading", "description": "Request for meter reading"},
        {"name": "Billing Inquiry", "description": "Questions about billing"},
        {"name": "Service Maintenance", "description": "Request for equipment maintenance"},
        {"name": "Connection Request", "description": "New gas connection request"}
    ]

    # Create Customer Accounts
    customer_accounts_data = [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone_number": "123-456-7890",
            "address": "123 Main St, Anytown, USA",
            "account_number": "ACCT-001"
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com", 
            "phone_number": "987-654-3210",
            "address": "456 Oak Ave, Somewhere, USA",
            "account_number": "ACCT-002"
        }
    ]

    # Add request types
    print("Creating Request Types...")
    for rt in request_types_data:
        response = requests.post(f'{BASE_URL}request-types/', json=rt)
        print(f"Created Request Type: {rt['name']} - Status: {response.status_code}")

    # Add customer accounts
    print("\nCreating Customer Accounts...")
    for account in customer_accounts_data:
        response = requests.post(f'{BASE_URL}customer-accounts/', json=account)
        print(f"Created Account: {account['name']} - Status: {response.status_code}")

def test_customer_requests():
    """
    Test customer request submission and tracking
    """
    print("\n--- Customer Request Testing ---")
    
    # Test Service Request Submission
    customer_request = {
        "customer_name": "John Doe",
        "customer_email": "john.doe@example.com",
        "customer_phone": "123-456-7890",
        "request_type": 1,  # Assuming first request type
        "description": "My gas meter seems to be malfunctioning"
    }

    # Submit Service Request
    print("Submitting Service Request...")
    response = requests.post(f'{BASE_URL}customer/requests/', json=customer_request)
    print(f"Request Submission Status: {response.status_code}")
    submitted_request = response.json()
    print("Submitted Request Details:")
    print(json.dumps(submitted_request, indent=2))

    # Track Service Request
    print("\nTracking Service Request...")
    track_params = {
        'request_id': submitted_request['id'],
        'email': 'john.doe@example.com'
    }
    response = requests.get(f'{BASE_URL}customer/requests/track_request/', params=track_params)
    print(f"Request Tracking Status: {response.status_code}")
    tracked_request = response.json()
    print("Tracked Request Details:")
    print(json.dumps(tracked_request, indent=2))

def test_support_representative_actions():
    """
    Test support representative actions
    """
    print("\n--- Support Representative Testing ---")
    
    # List all requests
    print("Listing All Requests...")
    response = requests.get(f'{BASE_URL}support/requests/')
    print(f"Request List Status: {response.status_code}")
    requests_list = response.json()
    print(f"Total Requests: {len(requests_list)}")

    # Update request status (if any requests exist)
    if requests_list:
        first_request = requests_list[0]
        update_data = {
            "status": "IN_PROGRESS",
            "support_notes": "Investigating the reported issue"
        }
        
        print("\nUpdating Request Status...")
        response = requests.patch(f'{BASE_URL}support/requests/{first_request["id"]}/update_status/', json=update_data)
        print(f"Request Update Status: {response.status_code}")
        updated_request = response.json()
        print("Updated Request Details:")
        print(json.dumps(updated_request, indent=2))

def main():
    create_sample_data()
    test_customer_requests()
    test_support_representative_actions()

if __name__ == '__main__':
    main()