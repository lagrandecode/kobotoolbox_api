from multiprocessing import context
from re import sub
from urllib import response
from django.shortcuts import render

# Create your views here.


#To display kobotoolbox data to website. This is the code for Django
def home(request):
    import json 
    import requests

    #Kobotoolbox provides Token for all users by using https://kobo.humanitarianresponse.info/token  
    header = {
        "Authorization": "Token 0d0f1372fdc030d7a53902ccd59552196cc9f462"
    }

    # Accessing the kobotoolbox API with the url ttps://kobo.humanitarianresponse.info/api/v2/assets/
    # To access the actual data, Kobotoolbox provides api/v1/data
    # In my case https://kc.humanitarianresponse.info/api/v1/data/1184899
    # So, I can changed the url to access the actual information like name, gender, or what was designed.

    response = requests.get('https://kobo.humanitarianresponse.info/api/v2/assets/aSq6uc8mEAVAPLn7YjFB4X/export-settings/esN8sabLW2cjjRidZruvin8.json',
    headers=header,auth=("kobotutor101","08078011943"))
    print(response.text)

    api = json.loads(response.content)
    context = {
        'api': api
    }
    return render(request,'home.html', context)
#     # With this code kobotoolbox data can be displayed on the web interface using Django 
#     # Working perfectly 100%
#     #if you fill the form on web or mobile the data will display in real-time



#For my Youtube Tutorial Oluwaseun Ogunmolu
# Using kobotoolbox for feedback on my website
# def home(request):
#     import json 
#     import requests
#     header = {
#         "Authorization": "Token 0d0f1372fdc030d7a53902ccd59552196cc9f462"
#     }
#     #Imagine I want to submit gender and age questions
#     submission = {
#         "Gender": "male",
#         "Age": "99",
#     }

#     #Here I'm printing the output
#     for i in submission:
#         print(i)
#     response = requests.post('https://kc.humanitarianresponse.info/api/v1/data/1184899.json',
#     headers=header,data=submission, 
#     auth=("kobotutor101","08078011943"))

#     print(response.text)
#     return render(request,'home.html',submission)
# #     #error message
# #     #{"detail":"Method \"POST\" not allowed."}
# #     #Please I need help 🙏

    

