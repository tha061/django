from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def index(request):
    form = UserCreationForm()
    return render(request, 'account/signup.html', {'form':form})
