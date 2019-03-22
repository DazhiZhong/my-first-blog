from django.contrib import admin
from django.urls import path, include
from .views import blog_detail_view,blog_outline_view,user_login_view,blog_pay_view,blog_cart_view,del_cart_view,pay_cart_view
app_name = 'Blog'
urlpatterns = [
    path('outline/',blog_outline_view,name='blog_outline'),
    path('detail/<int:blog_id>/',blog_detail_view,name='blog_detail'),
    path('login/',user_login_view,name='users_login'),
    path('pay/<int:blog_id>/',blog_pay_view,name='blog_pay'),
    path('cart/',blog_cart_view,name='blog_cart'),
    path('cart/<int:cart_id>/',del_cart_view,name='blog_cart_del'),
    path('cart/pay/',pay_cart_view,name='blog_cart_pay'),

]