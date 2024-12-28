from django.urls import path
from . import views

urlpatterns = [
     
 path('log', views.login1),
 path('admin1',views.admin_home),
  path('home',views.user_home),
]