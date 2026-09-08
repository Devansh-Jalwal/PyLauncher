import requests
import urllib.request
import json
import time

def get_random_fact():
    # Correct backend endpoint URL for random facts
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    
    # Request JSON response format explicitly 
    headers = {"Accept": "application/json"}
    
    # Set language preference query parameters to English
    params = {"language": "en"}
    
    try:
        # Perform the HTTP GET network request
        response = requests.get(url, headers=headers, params=params)
        
        # Verify the server responded with a successful status code (200)
        if response.status_code == 200:
            # Parse the clean JSON structural dictionary safely
            data = response.json()
            
            # Print the relevant text data fields
            print("\n================ SUCCESS ================")
            print(f"Fact: {data.get('text')}")
            print(f"Source: {data.get('source')}")
            print("=========================================\n")
        else:
            print(f"\n[Error] Server returned status code: {response.status_code}")
            print("The data sent by the server was not a fact.")
            
    except requests.exceptions.RequestException as error:
        # Catch network loss, connection timeouts, or bad address errors
        print(f"\n[Network Error] Could not connect to the API: {error}")
    except ValueError:
        # Catch instances where response is HTML or text instead of valid JSON
        print("\n[Parsing Error] The server response was not valid JSON.")
        print("Raw Server Output:")
        print(response.text)

# Execute the function
if __name__ == "__main__":
    get_random_fact()

