from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request): 
    return HttpResponse('<html><title>To-Do Lists</title><br/><h1><center><bold>To-Do Lists</bold></center><br/></h1></html>')