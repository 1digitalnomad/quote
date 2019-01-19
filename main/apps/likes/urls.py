from django.conf.urls import url
from . import views

#this is your likes app urls.

urlpatterns = [
    url(r'^create$', views.create, name='create')

]
