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
    fullcaps = (request.GET.get('fullcaps' , 'default'))
    removeline = (request.GET.get('removeline' , 'default'))
    countchar = (request.GET.get('countchar' , 'default'))
    removeextraspace = (request.GET.get('removeextraspace' , 'default'))
    print(removepun)
    print(djtext)

    if removepun == "on":
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

    
    elif(fullcaps == "on"):
         analyzed = ""
         for char in djtext:
              analyzed = analyzed + char.upper()

         params={
             'purpose':'Text Capitilization',
             'analyzed_text':analyzed
        }
         return render(request , "analyze.html" , params)

    elif(fullcaps == "on"):
             analyzed = ""
             for char in djtext:
                  if char !="\n":
                       analyzed = analyzed + char
                  
    
             params={
                 'purpose':'New lineremover',
                 'analyzed_text':analyzed
            }
             return render(request , "analyze.html" , params)

    elif(removeextraspace=="on"):
         analyzed = ""
         for index , char in enumerate(djtext):
              if not (djtext[index] == " " and djtext[index + 1] == " "):
                   analyzed = analyzed + char
                 
        
         params={
             'purpose':'Extra space Remover',
             'analyzed_text':analyzed,
        }
         return render(request , "analyze.html" , params)

    elif(countchar == "on"):
         count = 0
         for char in djtext:
              count = count + 1

         params={
              'purpose' : "Total character count ",
              'analyzed_text' :count
         }
         return render(request , "analyze.html" , params)

        


    
    
             

    
    else:
         return HttpResponse("Check the box to remove punctuation")
    
    



