from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='index'),
    url(r'^recipe$', views.recipePage, name='recipe'),

]
