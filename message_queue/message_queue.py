# from queue import Queue
# import threading
# import requests
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# message_queue = Queue()

# def publish_message(event_type, data):
#     message_queue.put({"event_type": event_type, "data": data})

# def handle_messages():
#     while True:
#         message = message_queue.get()
#         if message["event_type"] == "order_placed":
#             # Call inventory service to update stock
#             requests.post("http://localhost:8001/inventory/update-stock/", json=message["data"])

# # Start a thread for handling messages
# thread = threading.Thread(target=handle_messages, daemon=True)
# thread.start()


from queue import Queue
import threading
import requests
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

message_queue = Queue()

def publish_message(event_type, data):
    logging.info(f"Publishing message: {event_type} - {data}")
    message_queue.put({"event_type": event_type, "data": data})

# def handle_messages():
#     while True:
#         message = message_queue.get()
#         logging.info(f"Processing message: {message}")
#         if message["event_type"] == "order_placed":
#             try:
#                 response = requests.post(
#                     "http://localhost:8001/update-stock/", json=message["data"]
#                 )
#                 if response.status_code == 200:
#                     logging.info("Inventory updated successfully.")
#                 else:
#                     logging.error(f"Failed to update inventory: {response.text}")
#             except Exception as e:
#                 logging.error(f"Error while updating inventory: {str(e)}")


def handle_messages():
    while True:
        message = message_queue.get()
        if message["event_type"] == "order_placed":
            retries = 3
            while retries > 0:
                try:
                    response = requests.post(
                        "http://localhost:8001/inventory/update-stock/", json=message["data"]
                    )
                    if response.status_code == 200:
                        logging.info("Inventory updated successfully.")
                        break
                    else:
                        logging.error(f"Failed to update inventory: {response.text}")
                except requests.RequestException as e:
                    logging.error(f"Error: {e}")
                retries -= 1
                time.sleep(2 ** (3 - retries))


# Start a thread for handling messages
thread = threading.Thread(target=handle_messages, daemon=True)
thread.start()
