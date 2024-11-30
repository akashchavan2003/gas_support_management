Gas Utility Customer Service System
Project Overview
This Django application provides a comprehensive customer service platform for a gas utility company, allowing customers to submit and track service requests, and enabling customer support representatives to manage these requests.
Key Features

Submit service requests online
Track service request status
View customer account information
Support representatives can manage and update requests

Endpoints
Customer Endpoints

Submit Service Request

POST /customer/requests/
Allows customers to submit a new service request


List Customer Requests

GET /customer/requests/?email=customer@example.com
Retrieves all service requests for a specific customer


Track Specific Request

GET /customer/requests/track_request/?request_id=X&email=customer@example.com
Track status of a specific request



Support Representative Endpoints

List All Requests

GET /support/requests/
Optional query param: ?status=PENDING


Update Request Status

PATCH /support/requests/{request_id}/update_status/
Update request status and add support notes



Additional Endpoints

GET /request-types/: List available service request types
GET /customer-accounts/: Retrieve customer account information

Models

ServiceRequest: Tracks individual service requests
ServiceRequestType: Predefined service request categories
CustomerAccount: Customer account information

Installation

Clone the repository
Create a virtual environment
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Start the server: python manage.py runserver

Note
Authentication is disabled for this example. In a production environment, you would want to add proper authentication and authorization.
