from django.urls import path
from . import views
urlpatterns = [
    path('', views.showHomePage, name='home'),
    path('todos/',views.getAlltodo, name='todos'),
]