from django.shortcuts import render, redirect, HttpResponse
from functools import wraps
from data_system import models
from utils import my_page
from django.contrib.auth import authenticate, login
from users import models as users
import time

# Create your views here.


def calculator(request):
    return render(request, 'calculator/calculator.html')