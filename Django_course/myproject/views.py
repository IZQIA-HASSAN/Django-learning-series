#i have created this file = Izqia 
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse('''<h1>Izqia is a Django Developer</h1>  <a href="https://github.com/IZQIA-HASSAN/Django-learning-series">Visit github repo for updated code.</a>''')


# def about(request):
#     return HttpResponse("this is about section")


