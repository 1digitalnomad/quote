from django.shortcuts import render, HttpResponse, redirect
from .models import Like

# Create your likes app views.


def create(request):
    Like.objects.add_like(request.POST)
    return redirect('quotes:dashboard')

