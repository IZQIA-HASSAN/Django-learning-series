#i have created this file = Izqia 
from django.http import HttpResponse
from django.shortcuts import render
import os

# def index(request):
#     return HttpResponse('''<h1>Izqia is a Django Developer</h1>  <a href="https://github.com/IZQIA-HASSAN/Django-learning-series">Visit github repo for updated code.</a>''')


def index(request):
    params = {'name' : 'izqia' , 'country' : 'pakistan'}
    return render(request , 'index.html', params)

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


