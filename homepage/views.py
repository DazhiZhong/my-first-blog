from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def homepage_view(request,*args,**kwargs):
    return redirect('Blog:users_login')

def fuck_view(request,*args,**kwargs):
    return render(request,'fuck2.html',{})

