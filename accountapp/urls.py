
from django.urls import include, path

from accountapp import admin
from accountapp.views import hello_world

app_name = 'accountapp'
urlpatterns = [

    path('login/',hello_world,name='login'),
    path('logout/',hello_world,name='logout'),
    path('create/',hello_world,name='hello_world'),
    path('hello_world/',hello_world,name='create'),
]