from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    header = {
        "Authorization": "Token 4605bc6fa1bc107993ea297fd0d32ef670398ed3"
    }
    


    kobo = requests.get('https://kobo.humanitarianresponse.info/api/v2/assets/azpMY3AfSzcU97PNQV9eb8.json',headers=header)
    api = json.loads(kobo.content)
    context = {
        'api' : api
    }
    return render(request, 'home.html', context)
