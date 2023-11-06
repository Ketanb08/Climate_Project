from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from datetime import datetime
from app.models import Climate
# Create your views here.

def home(request):
    if request.method == "POST":
        area = request.POST.get("area", "Enter valid Area code")
        climate=request.POST.get("climate","Enter valid Climate Type")
        if(area=="" and climate==""):
            info2=Climate.objects.all()
            print(info2.count())
            return render(request, "index.html", {"info2": info2})
        elif (area=="Enter valid Area code") or (area==""):
            info=Climate.objects.filter(climate=climate).first()
        elif(climate=="Enter valid Climate Type" or (climate=="")):
            info=Climate.objects.filter(area=area).first()
        else:
            info=Climate.objects.filter(climate=climate,area=area).first()
        return render(request, "index.html", {"info": info})
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

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
    if request.method=="POST":
        climate=request.POST.get('climate')
        temperature=request.POST.get('temperature')
        area=request.POST.get('area')
        humidity=request.POST.get('humidity')
        chances=request.POST.get('chances')
        condition=Climate(climate=climate,temperature=temperature,area=area,chances=chances,humidity=humidity,date=datetime.today())
        condition.save()
    return render(request,'data.html')
    
def changedata(request):
    if request.method=="POST":
        area=request.POST.get("area","No Information")
        obj=Climate.objects.filter(area=area).first()
        newclimate=request.POST.get("newclimate","No Information")
        oldclimate=request.POST.get("oldclimate","No Information")
        obj.climate=newclimate
        obj.save()
    return render(request,'data.html')

def contact(request):
    return render(request,'contact.html')