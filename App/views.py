from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Users


def insert(request):
    u=request.POST.get("username")
    p=request.POST.get("password")
    user=Users(username=u,password=p)
    user.save()
    return HttpResponse("inser")

def index(request):
    return render(request,"index.html")