from django.shortcuts import render, redirect
from accounts.models import *
from blog.models import Category, Blog
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import auth_logout
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your views here.
@login_required
def profile(request):
    return render(request, "main_app/profile.html")

@login_required
def submit_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        image = request.FILES.get('image', 'common/logo.png')
        content = request.POST['content']
        if title and category and image and content:
            try:
                category_ob = Category.objects.get(name=category)
                blog = Blog(title=title, author=request.user.username,slug=slugify(title),featured_image=image, category=category_ob,content=content,date=datetime.today().strftime('%Y-%m-%d'))
                blog.save()
                messages.success(request,"Article posted for review")
            except Category.DoesNotExist:
                messages.error(request,"Some Error Occured!")
    allcat = Category.objects.all()
    all_dict = {"allcat": allcat}
    return render(request, "main_app/submit_article.html", all_dict)


@login_required
def my_articles(request):
    allpost = Blog.objects.filter(slug=slug)
    blog_dict = {"allpost": allpost}
    return render(request, 'blog/blog.html', blog_dict)


@login_required
def user_logout(request):
    logout(request)
    messages.success(request,"Successfully Loged out")
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    # Log out the user.
    # Return to homepage.

    

def user_register(request):
    registered = False
    if request.method == 'POST':
        name = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        # img = request.FILES.get('image', 'common/logo.png')
        
        # Check Validation
        # Validations Handled
        try:
            validate_email(email)
            if(pass1==pass2):
                if(len(pass1)>7):
                    
                    try:
                        match = Account.objects.get(email=email)
                        messages.error(request,"User with same email already exist!!")
                        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

                    except Account.DoesNotExist:
                            myuser = Account.objects.create_user(email,name,pass1)
                            myuser.save()
                            messages.success(request,"Account Successfully Created Now You can Login")
                            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                
                else:
                    messages.error(request,"Passwords Should be more than 8 characters!!")
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

            else:
                messages.error(request,"Passwords are Not Matching")
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))                              
        
        
        except ValidationError as e:
            messages.error(request,"Enter a valid email address!!")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))          
        # Validations Handled



        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        # Was not an HTTP post so.
        return HttpResponse('404 - Not Found')



def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        email = request.POST['lemail']
        password = request.POST['lpassword']

        # Django's built-in authentication function:
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Succecfull")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            messages.error(request,"Invalid")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        return HttpResponse("404 Error")
