from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']
        pwd1 = request.POST['password1']
        if pwd == pwd1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Registered Already')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, first_name=f_name, last_name=l_name, email=email,
                                                password=pwd)
                user.save();
                print('User Created')
                return redirect('login')

        else:
            messages.info(request, 'Passwords Not Matching')
            return redirect('registration')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=username, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid User')

            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
