from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(request,*args,**kwargs):
    print(request.user)
    return render(request,'home1.html',{})

def fuck_view(request,*args,**kwargs):
    return render(request,'fuck2.html',{})

