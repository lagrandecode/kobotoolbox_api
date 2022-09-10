from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    header = {
        "Authorization": "Token 0d0f1372fdc030d7a53902ccd59552196cc9f462"
    }
    


    kobo = requests.get('https://kc.humanitarianresponse.info/api/v1/data/1180169.json',headers=header)
    api = json.loads(kobo.content)

    for element in api:
        print(element)

    context = {
        'api' : api,
    }
    
    return render(request, 'home.html', context)
