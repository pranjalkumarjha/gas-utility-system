from django.shortcuts import render, HttpResponse
from home import user_login_verify   
from home import service_login_verify 
from home import get_all_request 
from home import all_requests_card 
from home import update_status_implement 
from home import generating_user_page 
from home import create_request  
from datetime import date
import asyncio
# Create your views here. 
def get_date():
    today_date = date.today() 
    today_date_str = today_date.strftime("%Y-%m-%d") 
    return today_date_str 

async def home(request):  
   return render(request,'home.html')  
   
async def user_login(request): 
     if request.method == 'POST':
      username = request.POST['username'] 
      password = request.POST['password']  
      print('here')
      val = await user_login_verify.verify_user(username,password) 
      
      if val:
            requests = await generating_user_page.generating_user_info()
            return render(request, 'user_page.html', {'requests': requests,'username':username})
           
      else:
          return HttpResponse('user not found') 
     else:
         return render(request,'user_login_page.html')
    
async def service_login(request): 
    if request.method == 'POST':
      username = request.POST['username'] 
      password = request.POST['password'] 
      val = await service_login_verify.verify_user(username,password)
      if val:  
           requests = await all_requests_card.return_card()
           
           return render(request, 'service_page.html', {'requests': requests})
      else:
          return HttpResponse('customer service not found') 
    else:
        return render(request,'service_login_page.html') 

async def update_status(request):
    if request.method=='POST': 
        username = request.POST['username'] 
        updated_status = request.POST['updated_status']  
        request_type = request.POST['request_type'] 
        await update_status_implement.update_status(username,updated_status,request_type)  
        return HttpResponse(1) 

async def open_issue(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        request_type = request.POST['request_type']   
        today_date_str = get_date()

        val = await user_login_verify.verify_user(username,password) 
        if val:  
            await create_request.add_request(username,today_date_str,request_type,'open') 
            return HttpResponse('added request') 
        else: 
            return HttpResponse('wrong username or password') 
    
           