
from django.urls import include, path

from acountapp import admin
from acountapp.views import hello_world

app_name = 'accountapp'
urlpatterns = [

    path('login/',hello_world,name='hello_world'),
    path('logout/',hello_world,name='hello_world'),
    path('create/',hello_world,name='hello_world'),
    path('hello_world/',hello_world,name='hello_world'),
]