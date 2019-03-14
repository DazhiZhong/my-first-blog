"""djgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homepage.views import homepage_view,fuck_view
from breakfast.views import breakfast_product_view,create_breakfast_view,create_new_b_view
urlpatterns = [
    path('',homepage_view,name='ass'),
    path('admin/', admin.site.urls),
    path('fuck/',fuck_view),
    path('bf/',include('breakfast.url')),
    path('blog/', include('blog.urls'))
    
    #path('breakfast/',breakfast_product_view,name='bb'),
    #path('b/<int:b_id>/',create_breakfast_view,name='b_number'),
    #path('bb/',create_new_b_view)
]
