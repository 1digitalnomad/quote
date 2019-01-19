from django.conf.urls import url
from . import views

#this is the users urls
urlpatterns = [
    url(r'^register$', views.create, name='create'),
    url(r'^(?P<id>\d+)$', views.my_quotes, name='my_quotes'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),

]
