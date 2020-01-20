from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Link
from . import forms
from .functions import returnZ
from .searching_mobile_apps_ids import *


# Create your views here.
def index(request):
    latest_link_list = Link.objects.order_by('-pub_date')[:5]
    context = {'latest_link_list': latest_link_list}
    return render(request, 'uploads/index.html', context)

def detail(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return render(request, 'uploads/detail.html', {'link': link})

def results(request):

    if request.method == 'POST':

        form = forms.CreateLink(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.firstChar = returnZ(instance.link_text)
            defineURL(instance.link_text)

            instance.save()

            print("FORM IS VALID DUDE")
            return redirect('uploads:results')
    else:
        form = forms.CreateLink()
    return render(request, 'uploads/detail.html', {'form':form} )

def vote(request, link_id):
    return HttpResponse("You're voting on link %s." % link_id)

def uploadHere(request):
    form = forms.CreateLink()
    return render(request, 'uploads/uploads.html', {'form':form})
