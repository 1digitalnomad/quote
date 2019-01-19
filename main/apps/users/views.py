from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views for users here.


def create(request):
    if request.method != 'POST':
        return redirect('quotes:index')
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('quotes:index')
    user = User.objects.create_user(request.POST)
    request.session['user_id'] = user.id
    return redirect('quotes:dashboard')

def my_quotes(request, id):
    if 'user_id' not in request.session:
        return redirect('quotes:index')
    context = {
        'myquotes' : User.objects.get(id=id).posted_by.all(), 
        'user' : User.objects.get(id=id)
    }
    return render(request, 'quotes/userposts.html', context)

def update(request):
    response = "this is the update link"
    return HttpResponse(response)
    # errors = User.objects.validate(request.POST)
    # if errors:
    #     for error in errors:
    #         messages.error(request, error)
    #         return redirect('myaccount:edit_page')
    # User.objects.update_user(request.POST, id)
    # return redirect('myaccount:edit_page')

def login(request):
    if request.method != 'POST':
        return redirect('quotes:index')
    valid, response = User.objects.login_user(request.POST)
    if valid == True:
        request.session['user_id'] = response
        return redirect('quotes:dashboard')
    else:
        messages.error(request, response)
    return redirect('quotes:index')


def logout(request):
    request.session.clear()
    return redirect('quotes:index')
