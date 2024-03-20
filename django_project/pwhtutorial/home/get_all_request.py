import json 
import asyncio
async def get_all_requests():  
    c=0
    with open('statuses_of_requests.json', 'r') as json_file:
     data = json.load(json_file)  
       
     requests = data['requests']
    #  for user in users: 
        
    #     if(user["username"]== username and user["password"]==password):
    #        c=1 
    # return c
     return requests