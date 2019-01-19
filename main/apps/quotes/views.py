from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..users.models import User
from .models import Quote
from ..likes.models import Like
# Create your quotes app views.

def index(request):
    return render(request, 'quotes/index.html')

#"This is the quotes and add page"
def show(request):
    if 'user_id' not in request.session:
        return redirect('quotes:index')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'quotes': Quote.objects.all(),
        'allusers' : User.objects.all(),
        'likes' : Like.objects.all()
    }
    return render(request, 'quotes/quotes.html', context)

#this is the create a quote link
def create(request):
    errors = Quote.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('quotes:dashboard')
    Quote.objects.create_quote(request.POST)
    return redirect('quotes:dashboard')

def edit(request, id):
    context = {
        'user_info' : User.objects.get(id=id)
    }
    return render(request, 'quotes/editpage.html', context)

def update(request, id):
    errors = User.objects.update_validate(request.POST, id)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect ('quotes:edit_page', id)
    User.objects.update_user(request.POST, id)
    return redirect('quotes:edit_page' ,id)

def destroy(request, id):
    Quote.objects.delete_quote(id)
    return redirect ('quotes:dashboard')