from django.shortcuts import render, HttpResponse
from django.urls import path


# Create your views here.
def Translator2(request):
     print('dfdfdsdfdsdsd', request.POST.get('columns'))
     if request.method == 'POST':
          print(request.POST.get('columns'))
     
     return render(request, 'Translator2.html')

def About(request):
     return render(request, 'About.html')
        
