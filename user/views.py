from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'You are logged in!')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'User not found!')
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        # GET values from form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            messages.add_message(request, messages.ERROR, 'Passwords not matched!')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.WARNING, 'User already exist!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.WARNING, 'User already exist!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'User saved!')
                return redirect('login')
    else:
        return render(request, 'user/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You logout!')
        return redirect('index')
