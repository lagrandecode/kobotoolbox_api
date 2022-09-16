from urllib import response
from django.shortcuts import render

# Create your views here.

# def home(request):
#     import requests
#     import json
#     header = {
#         "Authorization": "Token 0d0f1372fdc030d7a53902ccd59552196cc9f462"
#     }
    


#     kobo = requests.get('https://kobo.humanitarianresponse.info/api/v2/assets/aNFCLuoysyPsCTQ8H6kB2V.json',headers=header)
#     api = json.loads(kobo.content)

#     for element in api:
#         print(element)

#     context = {
#         'api' : api,
#     }
    
#     return render(request, 'home.html', context)

def kobopost(request):
    import json 
    import requests
    header = {
        "Authorization": "Token 0d0f1372fdc030d7a53902ccd59552196cc9f462"
    }
    pasting = {
        "what_is_your_name": "seun",
        "Gender": "male",
        "Age": "99",
    }
    response = requests.post(request,'https://kobo.humanitarianresponse.info/api/v2/assets/aNFCLuoysyPsCTQ8H6kB2V.json',data=json.dumps(pasting),headers=header)
    print(response.json)

    

