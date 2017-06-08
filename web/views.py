from django.shortcuts import render

# Create your views here.

def mainPage(request):
    return render(request, 'web/index.html',{})

def recipePage(request):
    return render(request, 'web/recipe.html',{})

def recipeResultPage(request):
    params = request.GET["recipe_key"]

    return render(request, 'web/recipe_result.html',{'test': params})


def stuff(request):
    return render(request, 'web/stuff.html', {})

def footerProvision(request):
    return render(request, 'web/footerProvision/provision.html',{})

def advertising(request):
    return render(request, 'web/footerProvision/advertising.html',{})

def faq(request):
    return render(request, 'web/footerProvision/faq.html',{})

def complete(request):
    return render(request, 'web/footerProvision/complete.html',{})
