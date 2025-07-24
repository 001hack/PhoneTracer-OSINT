import phonenumbers
from phonenumbers import geocoder, carrier
import requests

# Function to check if a number is spam using the NumVerify API
def check_spam_status(phone_number):
    api_key = "YOUR_API_KEY"  # Replace with your NumVerify API key  
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    
    response = requests.get(url)
    data = response.json()
    
    # Check if the API response indicates spam
    if data.get("valid", False):
        if 'line_type' in data and data['line_type'] == "mobile":
            return "Not Spam"  # You can refine this logic as per the data returned
        else:
            return "Possible Spam"
    else:
        return "Invalid Number"
    
    response = requests.get(url)
    data = response.json()
    
    # Check if the response contains owner information
    if "name" in data:
        return data["name"]
    else:
        return "Owner name not available"

def start_phone_tracer(target):
    print(f"[+] PhonTracer v2.1 - OSINT")
    print(f"[*] Target: {target}")
    print(f"[*] Initiating trace....")
    
    # Parse the number
    p = phonenumbers.parse(target, None)
    
    # Get country information (geolocation)
    country = geocoder.description_for_number(p, "en")
    print(f"[+] Country: {country}")
    
    # Attempt to get the carrier (may provide operator info for region hints)
    operator = carrier.name_for_number(p, "en")
    print(f"[+] Operator: {operator}")
    
    # Check if the number is flagged as spam
    spam_status = check_spam_status(target)
    print(f"[+] Spam Status: {spam_status}")
    
    print(f"[+] Trace complete")

# Ask for the phone number to trace
if __name__ == "__main__":
    target_number = input("[?] Enter the phone number to trace (including country code, e.g., +91-9920969082): ")
    start_phone_tracer(target_number)
