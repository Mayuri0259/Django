from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1' : "THIS IS SENT",
        'variable2' : "THIS IS SENT AGAIN"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is service page")

def contact(request):
    if request.method =='POST':
        name = request.POST.get(name='name')
        email = request.POST.get(email='email')
        phone = request.POST.get(phone='phone')
        desc= request.POST.get(desc='desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")

    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")

