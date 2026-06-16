import requests
import json

try:

    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    
    if response.status_code == 200:

        users = response.json()

        print("User Details:")
     

        
        for user in users:
            print("Name :", user["name"])
            print("Email:", user["email"])
            print("Phone:", user["phone"])
           

        
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        print("Data saved to users.json")

    
        print("Total Users Fetched:", len(users))

    else:
        print("API Request Failed!")
        print("Status Code:", response.status_code)

except requests.exceptions.ConnectionError:
    print("Internet Connection Error!")

except requests.exceptions.Timeout:
    print("Request Timed Out!")

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("Operation Complete!")