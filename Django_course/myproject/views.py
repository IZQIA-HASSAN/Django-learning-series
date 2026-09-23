#i have created this file = Izqia 
from django.http import HttpResponse
import os

# def index(request):
#     return HttpResponse("hello")


# def about(request):
#     return HttpResponse("this is about section")


def index(request):
    file_path = os.path.join(os.path.dirname(__file__) , 'one.txt')
    try:
        with open(file_path , 'r' , encoding='utf-8') as f :
            content = f.read()
    except FileNotFoundError:
        content = "file not found error"

    return HttpResponse(f"<pre>{content}</pre>")

# def about(request):
#     return HttpResponse("this is about section")