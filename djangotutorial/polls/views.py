from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.

# mapping "index"
def index(request):
    # requires an entry in urls.py
    return HttpResponse("Ehlo werld! You're at the polls index.")
