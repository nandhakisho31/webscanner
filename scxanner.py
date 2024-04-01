import requests
from bs4 import BeautifulSoup
# the BeautifulSoup must be installed in older versions now it has to be installed as a new version BeautifulSoup4.
#Do this pip install comand line and install the modules and packages.

def scan_website(url):
    try:
        # It Send's an HTTP request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example: Check for the presence of forms on the page
            forms = soup.find_all('form')
# when we use find_all it automatically scans everything and no need to mention the specific url path of the website.
            if forms:
                print("Potential forms found on the page.")
            else:
                print("No forms found on the page.")

            # You can add more checks based on your security criteria these was a basic code writen to just check the form wheater they are present or not.

        else:
            print("Failed to retrieve the page. Status code: 200" )
            # response.status_code prints: status code 200 as the request is successfull

    except Exception as e:
        print("An error occurred: code 404")
#If the given url is invaild the above print statement will exicuted.

# run the code
url_to_scan = (" Entre  website url for Scan: ")

scan_website(input(url_to_scan))
#you need to provide url in terminal as we used input method.
