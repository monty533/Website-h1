from django.shortcuts import render , HttpResponse
from myapp.models import Contact
from django.contrib import messages
# Create your views here.
def index_view(request):
    return render(request,'index.html')

def about_view(request):
    # return HttpResponse('hello')
    return render(request,'about.html')

def service_view(request):
    # return HttpResponse('hello')
    return render(request,'service.html')

def contact_view(request):
    # return HttpResponse('hello')
    if request.method== 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name=name,email=email,phone=phone)
        contact.save()
        messages.success(request, 'Your massage has been sent.')
    return render(request,'contact.html')
