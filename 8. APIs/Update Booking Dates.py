"""
"""

# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://linkedin.com/in/sirajudinbadi79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡
# 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡 https://twitter.com/Sirajudin79 🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴🟡🔴


import requests
import json

# Authentication
auth_data = {"username": "admin", "password": "password123"}
auth_headers = {'Content-Type': 'application/json'}
auth_request = requests.post('https://restful-booker.herokuapp.com/auth', headers=auth_headers, json=auth_data)
auth_response = auth_request.json()
token = auth_response.get('token')

# Get previous booking information
previous_booking_info = requests.get("https://restful-booker.herokuapp.com/booking/1")

# Prepare updated booking information
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cookie': f'token={token}'  # Include the token in the Cookie header
}

json_data = {
    'firstname': 'James',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {'checkin': '2018-01-01', 'checkout': '2018-02-01'},
    'additionalneeds': 'Breakfast'
}

# PUT request to update booking information
updated_booking_info_response = requests.put("https://restful-booker.herokuapp.com/booking/1", headers=headers, json=json_data)

print(updated_booking_info_response.json())
