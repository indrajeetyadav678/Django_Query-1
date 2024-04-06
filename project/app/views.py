from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel

# Create your views here.

def home(request):
    # all_data=StudentModel.objects.all()
    # print(all_data)
    # return HttpResponse(all_data)

    all_data=StudentModel.objects.all()
    all_data1=all_data.values()
    print(all_data)
    return HttpResponse(all_data1)