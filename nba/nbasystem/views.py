from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms, template
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .forms import CreateUserForm
# from howdidu.forms import UserProfileForm
# from howdidu.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    return render(request,'nbasystem/home.html')

def loginpage(request):
    errors=""
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request, user)
            if(user.is_superuser):
                return redirect('adminhome')
            try:
                if(Student.objects.all().get(user=user)):
                    return render(request, "nbasystem/shome.html")
            except:
                try:
                    if(Faculty.objects.all().get(user=user)):
                        return render(request,"nbasystem/fhome.html")
                except:
                    try:
                        if(Parent.objects.all().get(user=user)):
                            return render(request, "nbasystem/phome.html")
        #else:
                 #return 
                    finally:
                        errors="User name or password is wrong"
          
    context={'errors':errors}
    return render(request,'nbasystem/login.html',context) 
def adminhome(request):
    if (request.user.is_authenticated==False):
        return redirect('home')
    if(request.user.is_superuser==False):
        return redirect('home')
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            if(request.POST.get('type')=='Student'):
                s=Student.objects.create(user=user,username=form.cleaned_data.get('username'),fname=form.cleaned_data.get('first_name'),lname=form.cleaned_data.get('last_name'),email=form.cleaned_data.get('email'),phn=request.POST.get('num'))
                s.save()
                messages.success(request,"Account has been successfully created")
                return redirect('loginpage')
            elif(request.POST.get('type')=='Faculty'):
                s=Faculty.objects.create(user=user,username=form.cleaned_data.get('username'),fname=form.cleaned_data.get('first_name'),lname=form.cleaned_data.get('last_name'),email=form.cleaned_data.get('email'),phn=request.POST.get('num'))
                s.save()
                messages.success(request,"Account has been successfully created")
                return redirect('loginpage')
            else:
                user.delete()
    context={'form':form}
    return render(request,'nbasystem/adminhome.html',context)


def register(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            s=Parent.objects.create(user=user,username=form.cleaned_data.get('username'),fname=form.cleaned_data.get('first_name'),lname=form.cleaned_data.get('last_name'),sid=request.POST.get('sid'),email=form.cleaned_data.get('email'),phn=request.POST.get('num'))
            s.save()
            messages.success(request,"Account has been successfully created")
            return redirect('loginpage')
    context={'form':form}
    return render(request,'nbasystem/register.html',context)

def logoutpage(request):
    logout(request)
    messages.success(request, "Logged out succesful")
    return redirect('home')


def shome(request):
    context={}
    return render(request,'shome.html',context) 

def fhome(request):
    context={}
    return render(request,'fhome.html',context)

def phome(request):
    context={}
    return render(request,'phome.html',context)

def search(request):
    students=Student.objects.all()
    facultys=Faculty.objects.all()
    parents=Parent.objects.all()
    context={'students':students,'facultys':facultys,'parents':parents}
    return render(request,'search.html',context) 
    
# @login_required
# def register_profile(request):
#     profile = UserProfile.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return index(request)
#         else:
#             print {form.errors}
#     else:
#         form = UserProfileForm()
#     return render(request, 'howdidu/register_profile.html', {'form': form})

# #profile page using user name as url
# @login_required
# def profile_page(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(request, 'howdidu/profile.html', {'profile_user': user})