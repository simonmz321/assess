from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from functools import wraps
from data_system import models
from utils import my_page
from django.contrib.auth import authenticate, login
from users import models as users
import time

# Create your views here.
from .main_calculator import get_data, doc_to_docx

def calculator(request):
    return render(request, 'calculator/calculator.html')


def upload_doc(request):
    file = request.FILES.get('file')
    file_path = './calculator/files/' + file.name
    with open(file_path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
            print(chunk)
    file_path = doc_to_docx.doc_to_docx(file_path)
    data, t_column = get_data.get_data(file_path)
    result = []
    result.append(t_column)
    result.append(data)
    # result = t_column.append(result)
    return JsonResponse(result,safe=False)