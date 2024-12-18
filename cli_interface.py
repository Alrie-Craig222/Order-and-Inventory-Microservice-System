# import requests

# ORDER_SERVICE_URL = "http://localhost:8000"
# INVENTORY_SERVICE_URL = "http://localhost:8001"

# def create_order():
#     product_id = input("Enter Product ID: ")
#     quantity = input("Enter Quantity: ")
#     response = requests.post(
#         "http://localhost:8000/order/",  # Replace with your actual API endpoint
#         json={"product_id": product_id, "quantity": quantity}
#     )
#     print("Status Code:", response.status_code)  # Debug: Check HTTP status code
#     print("Response Text:", response.text)      # Debug: View raw server response
#     print("Headers:", response.headers)         # Debug: Check response headers

#     if response.headers.get("Content-Type") == "application/json":
#         try:
#             print("Response:", response.json())
#         except requests.exceptions.JSONDecodeError as e:
#             print("JSON Decode Error:", e)
#     else:
#         print("Non-JSON response received.")

# def view_inventory():
#     response = requests.get("http://localhost:8001/inventory/")  # Replace with your actual API endpoint
#     print("Status Code:", response.status_code)  # Debug: Check HTTP status code
#     print("Response Text:", response.text)      # Debug: View raw server response
#     print("Headers:", response.headers)         # Debug: Check response headers

#     if response.headers.get("Content-Type") == "application/json":
#         try:
#             data = response.json()
#             for product in data:
#                 print(f"Product ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}")
#         except requests.exceptions.JSONDecodeError as e:
#             print("JSON Decode Error:", e)
#     else:
#         print("Non-JSON response received.")


# def main():
#     while True:
#         print("\n1. Create Order\n2. View Inventory\n3. Exit")
#         choice = input("Choose an option: ")
#         if choice == "1":
#             create_order()
#         elif choice == "2":
#             view_inventory()
#         elif choice == "3":
#             break
#         else:
#             print("Invalid choice!")

# if __name__ == "__main__":
#     main()


import requests

ORDER_SERVICE_URL = "http://localhost:8000"
INVENTORY_SERVICE_URL = "http://localhost:8001"

# Function to retrieve CSRF token
def get_csrf_token():
    response = requests.get(f"{ORDER_SERVICE_URL}/csrf-token/")  # Adjust URL if needed
    if response.status_code == 200:
        return response.json().get("csrfToken")
    else:
        print("Failed to retrieve CSRF token.")
        return None

# Function to create an order with CSRF protection
def create_order():
    csrf_token = get_csrf_token()  # Retrieve the CSRF token
    if not csrf_token:
        print("Error: CSRF token missing.")
        return
    
    product_id = input("Enter Product ID: ")
    quantity = input("Enter Quantity: ")
    
    headers = {
        "X-CSRFToken": csrf_token,  # Add CSRF token to the headers
    }
    
    response = requests.post(
        f"{ORDER_SERVICE_URL}/order/",  # Replace with your actual API endpoint
        json={"product_id": product_id, "quantity": quantity},
        headers=headers  # Include CSRF token in the request
    )
    
    print("Status Code:", response.status_code)  # Debug: Check HTTP status code
    print("Response Text:", response.text)      # Debug: View raw server response
    print("Headers:", response.headers)         # Debug: Check response headers

    if response.headers.get("Content-Type") == "application/json":
        try:
            print("Response:", response.json())
        except requests.exceptions.JSONDecodeError as e:
            print("JSON Decode Error:", e)
    else:
        print("Non-JSON response received.")

# Function to view inventory with CSRF protection (if needed)
def view_inventory():
    csrf_token = get_csrf_token()  # Retrieve the CSRF token (if required)
    if not csrf_token:
        print("Error: CSRF token missing.")
        return
    
    headers = {
        "X-CSRFToken": csrf_token,  # Add CSRF token to the headers (if needed)
    }
    
    response = requests.get(
        f"{INVENTORY_SERVICE_URL}/inventory/",  # Replace with your actual API endpoint
        headers=headers  # Include CSRF token in the request (if needed)
    )
    
    print("Status Code:", response.status_code)  # Debug: Check HTTP status code
    print("Response Text:", response.text)      # Debug: View raw server response
    print("Headers:", response.headers)         # Debug: Check response headers

    if response.headers.get("Content-Type") == "application/json":
        try:
            data = response.json()
            for product in data:
                print(f"Product ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}")
        except requests.exceptions.JSONDecodeError as e:
            print("JSON Decode Error:", e)
    else:
        print("Non-JSON response received.")

def main():
    while True:
        print("\n1. Create Order\n2. View Inventory\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            create_order()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
