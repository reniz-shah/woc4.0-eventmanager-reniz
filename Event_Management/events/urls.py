from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('home/',views.index,name='home'),
    path('event_reg/',views.event_reg,name='event_reg'),
    path('participate_reg/',views.participate_reg,name='participate_reg'),
    path('event/',views.register_event,name='register'),
    path('participate/',views.register_participate,name='register'),
    path('dashboard/',views.dashboard,name='register'),
    path('allEvents/',views.allEvents,name='allEvents')
]
