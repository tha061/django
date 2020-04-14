from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from uploads.models import Link
import pandas as pd


@login_required(login_url="/account/login")
def databaseHome(request):

    latest_question_list = Link.objects.order_by('id')[:5]
    output = ', '.join([q.link_text for q in latest_question_list])
    output2 = [1, 2, 3 ,4 , 5]
    print("REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    dictionary = {'list':output, 'listNum':output2}

    df = {'1': output, '1': output2 }
    column_names = ["a", "b"]

    data = {'name': output, 'test':output2}

    df = pd.DataFrame(data)

    print(df.to_html())

    print("TOOOO HTML")
    dfToHTML = df.to_html()

    return render(request, 'database/database.html',{'dataframe':dfToHTML})
