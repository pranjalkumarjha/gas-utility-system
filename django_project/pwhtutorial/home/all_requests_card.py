import json 
import asyncio
from home import get_all_request
async def return_card():
    
    requests = await get_all_request.get_all_requests()

    print(requests)
    return requests
