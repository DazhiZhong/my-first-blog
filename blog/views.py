from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .models import Blog,Users,Payment
from .forms import BlogForm,UserForm
import os,time
username = ''
users = {}
IF_LOGIN = False
timeboo = time.asctime()
usercart = []
cartdict = {}
totalprice = 0
allobjectswhole = Blog.objects.all()
pricedict = {}
mydict = {}
for objects in allobjectswhole:
    temp=objects.get_id()
    print(temp)
    mydict[temp]=objects.title
    pricedict[temp]=objects.price
    print(objects.price)
userdict = {}
def user_login_view(request):
    global username,userdict
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
        userdict[requestuser] = [[],0]
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

    global totalprice,usercart,cartdict,pricedict,mydict

    obj = Blog.objects.get(id=blog_id)

    allobjectswhole = Blog.objects.all()

    if request.method == 'POST':
        wow=users[requestuser]+"  -  "+str(mydict[blog_id])+'\n'
        usercart.append(str(mydict[blog_id]))
        userdict[requestuser][0].append(blog_id)
        userdict[requestuser][1] += pricedict[blog_id]
        print(userdict[requestuser])


    blogobject = {
        'blog':obj,
        'object':obj,
        'un':users[requestuser]
    }
    return render(request,'blog_detail.html',blogobject)


def blog_pay_view(request,blog_id):
    requestuser=str(request.user)
    if not(requestuser in users.keys()) : print('ass'); return redirect('Blog:users_login')

    allobjects = Payment.objects.all()
    mydict = {}
    for objects in allobjects:
        temp=objects.get_id()
    if request.method == 'POST':
        wow=users[requestuser]+mydict[blog_id]+'\n'
        print(wow)#mydict[blog_id]
    obj = Payment.objects.get(id=blog_id)
    print(obj.code)
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


def del_cart_view(request,cart_id):
    requestuser=str(request.user)
    if not(requestuser in users.keys()) : print('ass'); return redirect('Blog:users_login')
    userdict[requestuser][0].remove(cart_id)
    return redirect('Blog:blog_cart')

def pay_cart_view(request):
    requestuser=str(request.user)
    if not(requestuser in users.keys()) : print('ass'); return redirect('Blog:users_login')
    price = round(userdict[requestuser][1])
    return redirect('Blog:blog_pay',blog_id=price)


def blog_cart_view(request):
    requestuser=str(request.user)
    if not(requestuser in users.keys()) : print('ass'); return redirect('Blog:users_login')
    tempnum = 0
    tpnum = []
    delnum = []
    nametemp = {}
    pricetemp = {}
    ttprice = 0
    for num in userdict[requestuser][0]:
        delnum.append(num)
        tpnum.append(tempnum)
        ttprice += pricedict[num]
        nametemp[tempnum] = mydict[num]
        pricetemp[tempnum] = pricedict[num]
        tempnum += 1
    print(nametemp)
    print(ttprice)
    userdict[requestuser][1]=ttprice

    cart = {
        'names':nametemp.values,
        'price':pricetemp.values,
        'num':delnum,
        'count':tpnum,
        'totalprice':ttprice,
        '1':'000'
    }

    return render(request,'cart.html',cart)



def blog_make_view(request):
    create_form = BlogForm(request.POST,request.FILES)
    print(create_form.is_valid())
    if create_form.is_valid():
        print(request.FILES)
        print(create_form.cleaned_data['image'])
        create_form.save()
    forms = {
        'form':create_form
    }
    return render(request,'blog_create.html',forms)
