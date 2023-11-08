from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from datetime import datetime
from app.models import Climate,is_valid
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
    status=1
    all1=0
    if request.method == "POST":
        area = request.POST.get("area", "Enter valid Area code")
        climate=request.POST.get("climate","Enter valid Climate Type")
        if(area=="" and climate==""):
            info2=Climate.objects.all()
            print(info2.count())
            all1=1
            return render(request, "index.html", {"info2": info2,"status":status,"all1":all1})
        elif (area=="Enter valid Area code") or (area==""):
            info=Climate.objects.filter(climate=climate).first()
        elif(climate=="Enter valid Climate Type" or (climate=="")):
            info=Climate.objects.filter(area=area).first()
        else:
            info=Climate.objects.filter(climate=climate,area=area).first()
            print(info)
            if info==None:
                status=0
        print("status :",status)
        print ("Info :",info)
        if info==None:
            status=0
        return render(request, "index.html", {"info": info,"status":status})
    return render(request,'index.html',{"status":status})

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'temp.html')

def loginUser(request):
    return render(request,'login.html')

def logoutUser(request):
        logout(request)
        return render(request,'index.html')

def data(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'data.html')
        else:
            return render(request,'login.html')
    else:
        return redirect('login')

def setdata(request):
    exception=None
    success=None
    if request.method=="POST":
        climate=request.POST.get('climate')
        temperature=request.POST.get('temperature')
        area=request.POST.get('area')
        print(climate)
        print(type(climate))
        humidity=request.POST.get('humidity')
        chances=request.POST.get('chances')
        condition=Climate(climate=climate,temperature=temperature,area=area,chances=chances,humidity=humidity,date=datetime.today())
        print("output",is_valid(climate,int(area)))
        if is_valid(climate,int(area))==1:
            condition.save()
            success="success"
        else:
            exception="Invalid Form Fields"
            return render(request,'data.html',{"exception":exception})
    return render(request,'data.html',{"success":success})
    
def changedata(request):
    old1=None
    new1=None
    area1=None
    success1=None
    if request.method=="POST":
        area=request.POST.get("area","No Information")
        obj=Climate.objects.filter(area=area).first()
        newclimate=request.POST.get("newclimate")
        oldclimate=request.POST.get("oldclimate")
        if(oldclimate==""):
            old1=1
            return render(request,'data.html',{"old1":old1})
        if(newclimate==""):
            new1=1
            return render(request,'data.html',{"new1":new1})
        if(area==""):
            area1=1
            return render(request,'data.html',{"area1":area1})
        obj.climate=newclimate
        obj.save()
        success1=1
    return render(request,'data.html',{"success1":success1})

def contact(request):
    return render(request,'contact.html')