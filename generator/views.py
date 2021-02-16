from django.shortcuts import render
from django.http import HttpResponse
import random 
# Create your views here.
def home(request):
     return render(request, 'generator/home.html')

def password(request):
     
     char = list('abcdefghijklmnopqrstuvwxyz')
     
     if request.GET.get('uppercase'):
          char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
     if request.GET.get('specialchar'):
          char.extend(list('!@#$%^&*()'))
     if request.GET.get('numbers'):
          char.extend(list('1234567890'))
     lenght = int(request.GET.get('Length'))
     
     thepassword = ''
     
     for x in range(lenght):
          thepassword += random.choice(char) 
     return render(request, 'generator/password.html',{'password':thepassword})

def about(request):
     return render(request, 'generator/about.html')

    