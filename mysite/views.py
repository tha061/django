from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from uploads.functions import *


def Home(request):

    #print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    print(getTextFromHTML('https://www.rosevilleplumbing.com.au/'))

    return render(request, 'mysite/home.html')



def about(request):

    print("we get to here")

    return render(request, 'mysite/about.html')
