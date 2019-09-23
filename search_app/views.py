from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from search_app.models import GameDataSet
import json
# import numpy as np
# import pandas as pd
# Create your views here.

def index(request):
	return render(request,'search_app/index.html')




def requested_game(request):
    input_value = request.GET.get('input_value', None)
    output_data =GameDataSet.objects.filter(title__contains=input_value).values_list('title','platform','score','genre','editors_choice')
    response_data={
    	'output_data':list(output_data)
    }
    return JsonResponse(json.dumps(response_data), safe=False)
