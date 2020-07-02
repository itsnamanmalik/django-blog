from django.shortcuts import render, redirect
from home.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

def privacy_policy(request):
    return render(request, 'main_app/privacy-policy.html')

def index(request):
    return render(request, 'main_app/index.html')
    

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = ContactForm(name=name, email=email, message=message)
        
        # Validations Handled
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request,"Enter a valid email address!!")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            if(len(name)>2 and len(message)>10):
                contact.save()
                messages.success(request,"Message Sent!!")
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            else:
                messages.error(request,"Message Or Name Is Too Short!!")
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        # Validations Handled
        
    else:
        return render(request, 'main_app/contact.html')


