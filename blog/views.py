from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .models import Blog,Users
from .forms import BlogForm,UserForm
import os,time
username = ''
users = {'AnonymousUser':'spooky guy'}
IF_LOGIN = False
timeboo = time.asctime()
usercart = []
cartdict = {}
totalprice = 0

def user_login_view(request):
    global username
    requestuser=str(request.user)
    print('login in')
    #if requestuser in users.keys(): return redirect('Blog:blog_outline')
    user_form = UserForm(request.POST or None)
    if user_form.is_valid():
        if username == '':
            user_form = UserForm(request.POST or None)
        user_form.save()
        username = str(user_form.cleaned_data['username'])
        users[requestuser] = username
        #if username in allusers: print('asshole')
        return redirect('Blog:blog_outline')
    user_form = UserForm(request.POST or None)
    created = {
        'form' : user_form       
    }
    return render(request, 'user_make.html', created)



def blog_detail_view(request,blog_id):
    requestuser=str(request.user)
    if not(requestuser in users.keys()) : print('ass'); return redirect('Blog:users_login')

    global totalprice,usercart,cartdict

    obj = Blog.objects.get(id=blog_id)

    allobjects = Blog.objects.all()
    pricedict = {}
    mydict = {}
    for objects in allobjects:
        temp=objects.get_id()
        print(temp)
        mydict[temp]=objects.title
        pricedict[temp]=objects.price

    if request.method == 'POST':
        wow=users[requestuser]+"  -  "+str(mydict[blog_id])+'\n'
        usercart.append(str(mydict[blog_id]))
        #print(usercart)
        totalprice += pricedict[blog_id]
        #print(wow,totalprice)#mydict[blog_id]
        tempdict = {
            'allcart':usercart,
            'totalprice':totalprice
        }
        cartdict[users[requestuser]]=tempdict
        print(cartdict[users[requestuser]]['allcart'])
        tempfile = open('./assets/text.txt','a')
        tempfile.write(wow)
        tempfile.close()


    blogobject = {
        'blog':obj,
        'object':obj,
        'un':users[requestuser]
    }
    return render(request,'blog_detail.html',blogobject)


def blog_pay_view(request,blog_id):
    requestuser=str(request.user)
    if not(requestuser in users.keys()) : print('ass'); return redirect('Blog:users_login')

    allobjects = Blog.objects.all()
    mydict = {}
    for objects in allobjects:
        temp=objects.get_id()
        mydict[temp]=objects.title
    if request.method == 'POST':
        wow=users[requestuser]+mydict[blog_id]+'\n'
        print(wow)#mydict[blog_id]
        tempfile = open('./assets/text.txt','a')
        tempfile.write(wow)
        tempfile.close()
    obj = Blog.objects.get(id=blog_id)
    
    blogobject = {
        'object':obj,
        'un':users[requestuser]
    }
    return render(request,'blog_pay.html',blogobject)


def blog_outline_view(request):
    requestuser=str(request.user)

    global username,IF_LOGIN
    if not(requestuser in users.keys()) : print('ass'); return redirect('Blog:users_login')
    all_obj = Blog.objects.all()
    print(username)
    blogobject = {
        'allblog':all_obj,
        'un':users[requestuser]

    }
    return render(request,'blog_outline.html',blogobject)

def blog_create_view(request):
    newblog = BlogForm(request.POST)
    if newblog.is_valid:
        newblog.save()
    newblog = BlogForm(request.POST)
    newblog_form = {
        'newform':newblog,
        'un':username

    }
    return render(request,'blog_create.html',newblog_form)
