from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.
# def home(request):
#     return render(request,'home.html')
def contact(request):
    if request.method=="POST":
      print('post')
      name=request.POST.get('name')
      email=request.POST.get('email')
      content=request.POST.get('content')
      number=request.POST.get('number')
      print(name,email,content,number)
      
      if len(name)>1 and len(name)<30:
          pass
      else:
          messages.error(request,'Invalid name')
          return render(request,'home.html')
      
      if len(email)>1 and len(email)<30:
          pass
      else:
          messages.error(request,'Invalid email')
          return render(request,'home.html')
      
      if len(number)>9 and len(number)<13:
          pass
      else:
          messages.error(request,'Invalid number')
          return render(request,'home.html')
      
      ins=models.Contact(name=name,email=email,content=content,number=number)
      ins.save()
      messages.success(request,'Thank you for connecting !')
      print('data saved to database')

    return render(request,'home.html')