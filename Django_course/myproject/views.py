#i have created this file = Izqia 
from django.http import HttpResponse
from django.shortcuts import render
import os



def index(request):
    params = {'name' : 'izqia' , 'country' : 'pakistan'}
    return render(request , 'index.html', params)

def analyze(request):
    djtext  = (request.GET.get('text' , 'default'))
    removepun = (request.GET.get('removepun' ,'default'))
    print(removepun)
    print(djtext)
    
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""


    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char

    params = {
        'purpose' : 'remove punctuation',
        'analyzed_text':analyzed

    }
    return render(request , "analyze.html" ,params )



