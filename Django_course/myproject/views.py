#i have created this file = Izqia 
from django.http import HttpResponse
import os

# def index(request):
#     return HttpResponse('''<h1>Izqia is a Django Developer</h1>  <a href="https://github.com/IZQIA-HASSAN/Django-learning-series">Visit github repo for updated code.</a>''')


def index(request):
    return HttpResponse('''<h1>choose a pipeline from the list </h1> 
    
     <a href="/capitilizefirst">Capitilize First</a>
     <a href="/removepun">Remove pun</a>
    
       ''')

def removepun(request):
    return HttpResponse('''
    <a href="/">Back</a>
    <p>this is remove pun function </p>
     ''')

def capfirst(request):
    return HttpResponse('''
    <a href="/">Back</a>
    <p>this is capitilize first function </p>
     ''')


