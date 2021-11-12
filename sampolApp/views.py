from django.shortcuts import render
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .form import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class myIndexView(View):
    def get(self, request):
        register = login.objects.all()
        print(register)
        context = {
            'register': register,

        }
        return render(request, 'loginTest.html', context)