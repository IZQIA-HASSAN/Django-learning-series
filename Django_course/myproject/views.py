#i have created this file = Izqia 
from django.http import HttpResponse
from django.shortcuts import render
import os



def index(request):
    params = {'name' : 'izqia' , 'country' : 'pakistan'}
    return render(request , 'index.html', params)

def analyze(request):
    djtext  = (request.POST.get('text' , 'default'))
    removepun = (request.POST.get('removepun' ,'default'))
    fullcaps = (request.POST.get('fullcaps' , 'default'))
    removeline = (request.POST.get('removeline' , 'default'))
    countchar = (request.POST.get('countchar' , 'default'))
    removeextraspace = (request.POST.get('removeextraspace' , 'default'))
    print(removepun)
    print(djtext)

    

    if removepun == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        
        
        for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
        print(djtext)
        print(analyzed)
        params = {
                'purpose' : 'remove punctuation',
                'analyzed_text':analyzed
        
            }
        djtext = analyzed
        # return render(request , "analyze.html" ,params )

    
    if(fullcaps == "on"):
         analyzed = ""
         for char in djtext:
              analyzed = analyzed + char.upper()

         params={
             'purpose':'Text Capitilization',
             'analyzed_text':analyzed
        }
         djtext = analyzed
        #  return render(request , "analyze.html" , params)

    if(removeline == "on"):
             analyzed = ""
             for char in djtext:
                  if char !="\n" and char != "\r":
                       analyzed = analyzed + char
                  
    
             params={
                 'purpose':'New lineremover',
                 'analyzed_text':analyzed
            }
             djtext = analyzed
            #  return render(request , "analyze.html" , params)

    if(removeextraspace=="on"):
         analyzed = ""
         for index , char in enumerate(djtext):
              if not (djtext[index] == " " and djtext[index + 1] == " "):
                   analyzed = analyzed + char
                 
        
         params={
             'purpose':'Extra space Remover',
             'analyzed_text':analyzed,
        }
         djtext = analyzed
        #  return render(request , "analyze.html" , params)

    if(countchar == "on"):
         count = 0
         for char in djtext:
              count = count + 1

         params={
              'purpose' : "Total character count ",
              'analyzed_text' :count
         }
         djtext = analyzed

    return  render(request , "analyze.html" , params)

    

    
    
    
    



