from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
# Create your views here.

# functions to be called to render pages


def myview(request):
    return render(request, "index.html")


def getotp(request):
    if request.method == 'POST':
        print(request.POST.get('matricNumber', None))
        return HttpResponse({'message': 'success'})
    else:
        return render(request, 'getotp.html')


def votingpage(request):
    return render(request, "votingpage.html")


def submit(request):
    return render(request, "done.html")


def pollresult(request):
    return render(request, "trackerpage.html")
