from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/account/login")
def databaseHome(request):

    print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

    return render(request, 'database/database.html')
