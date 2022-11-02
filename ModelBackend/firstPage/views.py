from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import joblib

model = joblib.load('modelPipeline.pkl')

def scoreJson(request):
    
    return JsonResponse({'score': 1})

def scoreFile(request):
    return JsonResponse({'score': 1})

