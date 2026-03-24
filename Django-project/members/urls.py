from django.urls import path,include
from . import views


urlpatterns = [
    path('members/', views.members, name= 'members'),
    path('mymemb/',views.mymemb,name='mymemb'),
    path('mymemb/details/<int:id>',views.details,name='details'),
    path('',views.main, name='main'),
    path('testing/', views.testing, name='testing'),


]

