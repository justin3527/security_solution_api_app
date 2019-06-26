from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import getAllUser
from .models import ServerData
from django.views.decorators.csrf import csrf_exempt
from .tests import *
from .FirePower import *


def default(request):
   return render(request, "solution/default.html")
@csrf_exempt
def ise(request):
    
    #getAllUser().createUser()
    #getAllUser().changePW()
    serverInfo = ServerData.objects.filter(name="ISE")[0]
    solution = getAllUser(serverInfo)
    if request.method == "POST":
      
      print("post info : " + str(request.POST))
      dict = request.POST
      
      if str(dict['btn']) == "enter":
        ServerData(name="ISE", ip=str(dict['serverIP']), adminID=str(dict['adminID']), adminPW=str(dict['adminPW'])).save()
        serverInfo = ServerData.objects.filter(name="ISE")[0]
        solution = getAllUser(serverInfo)
        
      elif str(dict['btn']) == "create":
        print("create")
        solution.createUser(dict)
        
      elif str(dict['btn']) == "change":
        print("change")  
        solution.changePW(dict)
    
    
    
    return render(request, "solution/ise.html", {"solution":solution})

@csrf_exempt
def stw(request):
    stw = jwtTest("10.0.0.10","admin","Password1!")
    return render(request, "solution/stw.html",{"stw":stw})
    
@csrf_exempt
def firePower(request):

   fp = FirePower()
   print(request)
   print(request.method)
   
   if request.method == "POST":
     dict = request.POST
     print("post info : " + str(request.POST))
     if dict['serverIP'] != "" :
       #fp = FirePower(dict['serverIP'],dict['adminID'],dict['adminPW'])
       print(dict)
     
   fp = FirePower("10.0.0.20","admin","Password1!")
   return render(request, "solution/firepower.html",{"fp":fp})