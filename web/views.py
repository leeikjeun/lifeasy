from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import sys
import urllib.request

# Create your views here.


@csrf_exempt
def mainPage(request):
    return render(request, 'web/index.html',{})

@csrf_exempt
def SearchPage(request):

    print ("재료", request.POST)

    try:
        client_id = "az3VR2WRt2KHh5y8sswK"
        client_secret = "k6TRia1ymk"
        encText = urllib.parse.quote("검색할 단어")
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
    except Exception as E:
        print (E)





    return render(request, 'web/recipe_result.html', {})

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
