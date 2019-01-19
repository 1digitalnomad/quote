from django.conf.urls import url
from . import views

#this is your quotes app urls.

urlpatterns = [
    url(r'^quotes$', views.show, name='dashboard'),
    url(r'^create$', views.create, name='create'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)$', views.edit, name='edit_page'),
    url(r'^myaccount/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.destroy, name='delete')

]
