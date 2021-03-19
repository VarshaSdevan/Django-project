from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Event

      
      
def index(request):
    return render(request, 'base.html')

