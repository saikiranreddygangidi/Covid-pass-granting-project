
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import User_status
from django.contrib import messages
username=''
import logging



# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

'''def index(request):
    # Send the Test!! log message to standard out
    logger.error("Test!!")
    return HttpResponse("Hello logging world.")'''
def login(request):
    if request.method =='POST':
        global username
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:

            auth.login(request,user)
            #before info shown because level is warning now it is info
            #logger.error("logged in user is:"+username)
            logger.info("logged in user is:"+username)
            #logger.log("log logeed here")
            data=User_status.objects.get(username=username)
            return render(request,'user-data.html',{'data':data})
        else:
            messages.info(request,'invaild details')
            return redirect('login')  
    else:
       return render(request,'login.html')     
def logout(request):
    auth.logout(request)
    return render(request,'login.html')
def register(request):
    if request.method =='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        
        data=User_status(username=username,status="not-requested")
        data.save();
        user=User.objects.create_user(username=username,password=password);
        user.save();
        return render(request,'login.html')
    else:
       return render(request,'register.html')
# Create your views here.

def change(request):
    global username
    data=User_status.objects.get(username=username)
    data.status="requested"
    
    data.save();
    logger.info("Changed the user "+username+ " to requested")
    data1=User_status.objects.get(username=username)
    return render(request,'user-data.html',{'data':data1})



def access(request):
    data=User_status.objects.all();
    return render(request,'admin-access.html',{'data':data})
def grant_request(request,username):
    data=User_status.objects.get(username=username)
    data.status="granted"
    data.save();
    logger.info("GRANTED THE USER "+username)
    return redirect('/admin-access')