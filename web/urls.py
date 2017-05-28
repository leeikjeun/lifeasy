from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.firstPage, name='first'),
    url(r'^index$', views.mainPage, name='index'),
]
