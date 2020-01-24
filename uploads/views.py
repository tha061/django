from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Link
from . import forms
from .functions import *
from .searching_mobile_apps_ids0 import *
from .playStore import *
from .download_apk import *
#from googleplay_api.googleplay import GooglePlayAPI
from .trackinglibraries import *

print("KKKKKk")
print(file_size(r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\menloseweight.loseweightappformen.weightlossformen.apk'))
#get_app_metainfo('menloseweight.loseweightappformen.weightlossformen.apk')

#download_apk('menloseweight.loseweightappformen.weightlossformen', '1.0.8', r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\APKdump')
#print(app)
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
            download_apk(instance.link_text)
            instance.firstChar = returnZ(instance.link_text)
            instance.save()
            print("FORM IS VALID")
            return redirect('uploads:results')
    else:
        form = forms.CreateLink()
    return render(request, 'uploads/detail.html', {'form':form} )

def vote(request, link_id):
    return HttpResponse("You're voting on link %s." % link_id)

def uploadHere(request):
    form = forms.CreateLink()
    return render(request, 'uploads/uploads.html', {'form':form})
