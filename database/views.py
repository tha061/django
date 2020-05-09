from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from uploads.models import Link
from uploads.forms import CreateLink
import pandas as pd


@login_required(login_url="/account/login")
def databaseHome(request):
    queryset = list(reversed(Link.objects.all())) # list of objects

    context = {
        "object_list": queryset
    }

    print(queryset[260].author)

    return render(request, 'database/database.html', context)
