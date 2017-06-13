from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def mainPage(request):
    return render(request, 'web/index.html',{})

@csrf_exempt
def SearchPage(request):
    print ("재료", request.POST)
    return render(request, 'web/index.html', {})

@csrf_exempt
def recipePage(request):
    return render(request, 'web/recipe.html',{})

@csrf_exempt
def recipeResultPage(request):
    params = request.GET["recipe_key"]

    #print (params)

    return render(request, 'web/recipe_result.html',{'test': params})

@csrf_exempt
def stuff(request):
    return render(request, 'web/stuff.html', {})

@csrf_exempt
def footerProvision(request):
    return render(request, 'web/footerProvision/provision.html',{})

@csrf_exempt
def advertising(request):
    return render(request, 'web/footerProvision/advertising.html',{})

@csrf_exempt
def faq(request):
    return render(request, 'web/footerProvision/faq.html',{})

@csrf_exempt
def complete(request):
    return render(request, 'web/footerProvision/complete.html',{})
