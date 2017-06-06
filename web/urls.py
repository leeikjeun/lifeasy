from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainPage, name='index'),
    url(r'^recipe$', views.recipePage, name='recipe'),
    url(r'^recipe/result$', views.recipeResultPage, name='recipe_result'),
    url(r'^footer/service$', views.footerProvision, name='service'),
    url(r'^footer/advertising$', views.advertising, name='advertising'),
    url(r'^footer/faq$', views.faq, name='faq'),
]
