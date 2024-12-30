from django.urls import path
from . import views

urlpatterns = [
     
 path('log', views.login1),
 path('admin1',views.admin_home),
 path('department',views.add_department),
 path('staff',views.add_staff),
 path('view_staff',views.view_staff),
 path('home',views.user_home),
]