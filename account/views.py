from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def view_signup(request):
     if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             #  log the user in
             return redirect('account:view_login')

     else:
        form = UserCreationForm()
     return render(request, 'account/signup.html', { 'form': form })

def view_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('account:view_home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', { 'form': form })

def view_logout(request):
    print("ONE")
    username = request.user.username
    if(username == ""):
        username = "no account"
    print("TWO")
    logout(request)
    print("THREE")

    return render(request, 'account/logout.html', {'accountName': username } )

@login_required(login_url="/account/login")
def view_home(request):
    print("REEEEEEEEEEEEEEEEEEEEEEEEEEE")
    print(request)
    return render(request, 'account/home.html')
