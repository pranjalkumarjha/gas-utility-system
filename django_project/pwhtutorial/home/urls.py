from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home), 
    path('user_login', views.user_login), 
    path('service_login', views.service_login), 
    path('update_status', views.update_status), 
    path('open_issue', views.open_issue)

]
