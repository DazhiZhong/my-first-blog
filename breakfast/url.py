from django.contrib import admin
from django.urls import path, include
from homepage.views import homepage_view,fuck_view
from breakfast.views import breakfast_product_view,create_breakfast_view,create_new_b_view
app_name = 'bf'
urlpatterns = [
    path('breakfast/',breakfast_product_view,name='bb'),
    path('b/<int:b_id>/',create_breakfast_view,name='b_number'),# b_id used in models
    path('bb/',create_new_b_view)

]