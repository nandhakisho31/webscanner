import requests
from bs4 import BeautifulSoup

def scan_website(url):
    try:
        # Send an HTTP request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example: Check for the presence of forms on the page
            forms = soup.find_all('form')
            if forms:
                print("Potential forms found on the page.")
            else:
                print("No forms found on the page.")

            # You can add more checks based on your security criteria

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
url_to_scan = 'https://example.com'
scan_website(url_to_scan)
