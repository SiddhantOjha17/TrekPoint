from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def upcoming(request):
    treks = Treks.objects.all()
    context = {'treks': treks}
    return render(request, "library.html", context)

@csrf_exempt
def trek(request,hm):
    data = Treks.objects.filter(name = hm)
    context = {"data": data}
    return render(request, "treks.html", context)
