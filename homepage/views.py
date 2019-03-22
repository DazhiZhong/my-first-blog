from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def homepage_view(request,*args,**kwargs):
<<<<<<< HEAD
    return redirect('Blog:users_login')
=======
    #return redirect('Blog:users_login')
    return render(request,'home1.html',{})
>>>>>>> ade200fa5aa0f271ac01ecb9b627447f47b6979b

def fuck_view(request,*args,**kwargs):
    return render(request,'fuck2.html',{})

