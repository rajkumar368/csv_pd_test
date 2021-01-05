import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render

def final_response(request,day):
    df = pd.read_csv('HFT_test/hft.csv')
    days_data  = list(df.days)
    if day in days_data:
        q = f'days == {day}'
        day_index = days_data.index(day)
        result = df.query(q)['status'][day_index]
        return JsonResponse({'Message': result})
    else:
        return JsonResponse({'Error': 'Please check input once'})


def login(request):
    return render(request,'login.html')
        
    