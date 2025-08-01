#!/usr/bin/env python3
"""
Simple test script for the USSD API
"""

import requests
import json

def test_health_endpoint(base_url):
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{base_url}/health")
        print(f"Health check: {response.status_code} - {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_ussd_endpoint(base_url):
    """Test the USSD endpoint"""
    try:
        # Test initial menu
        data = {
            "sessionId": "test123",
            "serviceCode": "*123#",
            "phoneNumber": "+254700000000",
            "text": ""
        }
        response = requests.post(f"{base_url}/ussd", data=data)
        print(f"USSD initial menu: {response.status_code}")
        print(f"Response: {response.text}")
        
        # Test balance check
        data["text"] = "1"
        response = requests.post(f"{base_url}/ussd", data=data)
        print(f"USSD balance check: {response.status_code}")
        print(f"Response: {response.text}")
        
        return True
    except Exception as e:
        print(f"USSD test failed: {e}")
        return False

if __name__ == "__main__":
    # Test with local server (change URL for production)
    base_url = "http://localhost:8000"
    
    print("Testing USSD API...")
    print("=" * 50)
    
    health_ok = test_health_endpoint(base_url)
    ussd_ok = test_ussd_endpoint(base_url)
    
    print("=" * 50)
    if health_ok and ussd_ok:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!") 