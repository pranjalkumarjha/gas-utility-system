import json
import asyncio   
from datetime import date
async def update_status(username, new_status,request_type):
    with open('statuses_of_requests.json', 'r') as file:
        data = json.load(file)
    today_date = date.today() 
    date_str = today_date.strftime("%Y-%m-%d")
    for request in data['requests']:
        
        if request['username'] == username and request['request_type'] == request_type and request['request_status']!='closed':  # so that we cannot open a closed issue again as it may lead to frauds
            request['request_status'] = new_status 
            request['last_update']= date_str

            break
    
    with open('statuses_of_requests.json', 'w') as file:
        json.dump(data, file, indent=4)

