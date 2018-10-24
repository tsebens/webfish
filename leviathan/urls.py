from django.urls import path

from . import views

urlpatterns = [
    #Home page
    path('', views.Index, name='index')
]