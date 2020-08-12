from django.contrib import admin
from django.urls import path , include
from myapp import views

urlpatterns = [
    path('',views.index_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('service/',views.service_view,name='service'),
    path('contact/',views.contact_view,name='contact'),

]
