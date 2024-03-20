import json 
import asyncio
async def verify_user(username,password):  
    c=0
    with open('user_login_data.json', 'r') as json_file:
     data = json.load(json_file)  
       
     users = data['users']
     for user in users: 
        
        if(user["username"]== username and user["password"]==password):
           c=1 
    return c
