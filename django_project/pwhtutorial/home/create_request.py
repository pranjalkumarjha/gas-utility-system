import json
import asyncio
from datetime import date
async def add_request(username, request_date, request_type, request_status):
    # Create a dictionary for the new request 
    today_date = date.today() 
    today_date_str = today_date.strftime("%Y-%m-%d")
    new_request = {
        "username": username,
        "request_date": request_date,
        "request_type": request_type,
        "request_status": request_status,
        "last_update": today_date_str
    }

    # Read the existing JSON data
    with open('statuses_of_requests.json', 'r') as file:
        data = json.load(file)

    # Append the new request to the list of requests
    data["requests"].append(new_request)

    # Write the updated JSON data back to the file
    with open('statuses_of_requests.json', 'w') as file:
        json.dump(data, file, indent=4)

