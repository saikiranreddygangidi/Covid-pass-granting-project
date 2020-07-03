from django.urls import path
from . import views
urlpatterns=[path('',views.register,name='register'),
          
          
          path('login',views.login,name='login'),
          path('logout',views.logout,name='logout'),
      
          path('register1',views.register,name='register'),
           path('admin-access',views.access),
           path('grant_request/<slug:username>/',views.grant_request),
           path('change',views.change),]
