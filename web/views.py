from django.shortcuts import render

# Create your views here.

def mainPage(request):
    return render(request, 'web/index.html',{})

def recipePage(request):
    return render(request, 'web/recipe.html')

def stuff(request):
    return render(request, 'web/stuff.html', {})
