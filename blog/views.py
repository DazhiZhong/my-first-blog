from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from .models import Blog,Users
from .forms import BlogForm,UserForm
import os
username = ''
IF_LOGIN = False
def user_login_view(request):
    global username
    print('login in')
    user_form = UserForm(request.POST or None)

    if user_form.is_valid():
        username = str(user_form.cleaned_data['username'])
        if username != '':
            IF_LOGIN=True
            print('red:',username)
            return redirect('Blog:blog_outline')
        else:
            user_form = UserForm(request.POST or None)

    user_form = UserForm(request.POST or None)
    created = {
        'form' : user_form       
    }
    return render(request, 'user_make.html', created)



def blog_detail_view(request,blog_id):
    obj = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        return redirect('Blog:blog_pay',blog_id=blog_id)
    blogobject = {
        'blog':obj,
        'object':obj,
        'un':username
    }
    return render(request,'blog_detail.html',blogobject)


def blog_pay_view(request,blog_id):
    obj = Blog.objects.get(id=blog_id)
    
    blogobject = {
        'object':obj,
        'un':username
    }
    return render(request,'blog_pay.html',blogobject)


def blog_outline_view(request):
    global username,IF_LOGIN
    if username == '': print('ass'); return redirect('Blog:users_login')
    all_obj = Blog.objects.all()
    print(username)
    blogobject = {
        'allblog':all_obj,
        'un':username

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
