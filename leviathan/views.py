from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Index(request):
    return HttpResponse("Index for leviathan")

