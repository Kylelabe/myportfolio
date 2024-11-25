from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for the app
    path('contact/', views.index, name='contact'),

]

