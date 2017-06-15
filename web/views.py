from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
import sys
import urllib.request
import json

# Create your views here.


@csrf_exempt
def mainPage(request):
    return render(request, 'web/index.html',{})

@csrf_exempt
def SearchPage(request):

    From_Parent = request

    print ("재료", From_Parent.POST)

    Search_String = ""

    try:
        Page = int(From_Parent.GET['page'])
        print (Page)
    except:
        Page = 0

    if(Page == 0 or Page == 1):
        Start_index = 1
    else:
        Start_index = Page * 100

    try:
        Search_String = (From_Parent.GET['Search_String'])
    except:
        for row in From_Parent.POST:
            if (row=="page"):
                continue
            print (From_Parent.POST[row])
            if(Search_String == ""):
                Search_String = From_Parent.POST[row]
            else:
                Search_String = "{} 과 {}".format(Search_String, From_Parent.POST[row])



    print (Search_String)









    try:
        client_id = "09y9seGZ8bqyV1jcpRE9"
        client_secret = "jGX8gseiuw"
        encText = urllib.parse.quote(Search_String)
        url = "https://openapi.naver.com/v1/search/blog?display=100&start={}&query=".format(Start_index) + encText

        headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret" : client_secret}
        rqs = urllib.request.Request(url, None, headers)  # The assembled request


        response = urllib.request.urlopen(rqs)
        rescode = response.getcode()
        #print (response)
        if(rescode==200):
            response_body = response.read()
            decoded_data = json.loads(response_body.decode('utf-8'))

            Total = decoded_data['total']
            #print (decoded_data)
            #print(response_body.decode('utf-8'))
        else:
            pass
            #print("Error Code:" + rescode)

        List_String = list()

        for row in decoded_data['items']:
            List_String.append("""<div class="list">
  <a href="{0}">
    <div class="img-box">
      <img src="https://s17.postimg.org/j0qisnqfz/testfood.jpg" alt="">
    </div>
    <div class="result">
      <h3 class="result-name">{1}</h3>
      <p class="result-text">{2}</p>
    </div>
  </a>
</div>
""".format(row['link'],row['title'],row['description']))

        #print (List_String)

        print ("TOTAL: {}".format(Total))


    except Exception as E:
        print (E)

    return render(request, 'web/recipe_result.html', {'List_String':List_String,'Search_String':Search_String,'Total':Total})

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
