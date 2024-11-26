import requests
from bs4 import BeautifulSoup

def get_csrf_token(login_page_url):
    # Send GET request to fetch the login page
    login_page = requests.get(login_page_url)
    
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(login_page.text, 'html.parser')
    
    # Print the page content to inspect it
    print(soup.prettify())  # This will print the HTML content of the page
    
    # Try to find the CSRF token in the login form
    csrf_token_input = soup.find('input', {'name': 'ci_csrf_token'})
    if csrf_token_input:
        return csrf_token_input['value']
    else:
        return None  # If token is not found

# Example usage
login_url = "https://erp.bitdurg.ac.in/login.jsp"
csrf_token = get_csrf_token(login_url)
if csrf_token:
    print("CSRF Token:", csrf_token)
else:
    print("CSRF Token not found!")
