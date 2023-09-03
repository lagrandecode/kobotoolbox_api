from multiprocessing import context
from re import sub
from urllib import response
from django.shortcuts import render,redirect
import io
import uuid
from datetime import datetime
from .models import *
from .forms import *
# Create your views here.


#To display kobotoolbox data to website. This is the code for Django
def home(request):
    import json 
    import requests

    #Kobotoolbox provides Token for all users by using https://kobo.humanitarianresponse.info/token  
    header = {
        "Authorization": "Token 6fb29d8015dc136cba3558590282ddab7f2b24a5"
    }

    # Accessing the kobotoolbox API with the url ttps://kobo.humanitarianresponse.info/api/v2/assets/
    # To access the actual data, Kobotoolbox provides api/v1/data
    # In my case https://kc.humanitarianresponse.info/api/v1/data/1184899
    # So, I can changed the url to access the actual information like name, gender, or what was designed.

    response = requests.get('https://kc.kobotoolbox.org/api/v1/data/1589205?format=json',
    headers=header,auth=("ogunmolu_oluwaseun","08078011943"))
    print(response.content)
    # print(response.text)

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

# def format_openrosa_datetime():
#     return datetime.now().isoformat('T', 'milliseconds')

# def home(request):
#     import json 
#     import requests
#     header = {
#         "Authorization": "Token 6fb29d8015dc136cba3558590282ddab7f2b24a5"
#     }
#     #Imagine I want to submit gender and age questions
#     submission = {
#         "formhub/uuid": "43e93d84ef2341a89b562d41db6bd829",
#         "start": format_openrosa_datetime(),
#         "end": format_openrosa_datetime(),
#         "name": "kazeem",
#         "__version__": "vKMXGsXb7sEw42x2hnDqcf",
#         "_xform_id_string": "aK9ANfTMCGAQHNiunmQyki"
#     }

#     #Here I'm printing the output
#     for i in submission:
#         print(i)
#     response = requests.post('https://kc.kobotoolbox.org/api/v1/submissions',
#     headers=header,data=submission, 
#     auth=("ogunmolu_oluwaseun","08078011943"))
#     if response == 201:
#         return 'SUCCESS'
#     return 'error'

#     print(response.text)
#     print(response.content)
#     print(submission)
#     return render(request,'home.html',submission)
# #     #error message
# #     #{"detail":"Method \"POST\" not allowed."}
# #     #Please I need help 🙏

    

# kobotoolbox/views.py

import io
import requests
import uuid
from datetime import datetime


BASE_URL = 'https://kc.kobotoolbox.org'
SUMISSION_URL = f'{BASE_URL}/api/v1/submissions'
TOKEN = '6fb29d8015dc136cba3558590282ddab7f2b24a5'  # Replace with your KoboToolbox API token

def format_openrosa_datetime():
    return datetime.now().isoformat('T', 'milliseconds')

def create_xml_submission(data, _uuid):
    xml_data = f'''
    <aK9ANfTMCGAQHNiunmQyki id="aK9ANfTMCGAQHNiunmQyki" version="1 ({datetime.now():%Y-%m-%d %H:%M:%S})">
        <formhub>
            <uuid>43e93d84ef2341a89b562d41db6bd829</uuid>
        </formhub>
        <start>{format_openrosa_datetime()}</start>
        <end>{format_openrosa_datetime()}</end>
        <name>{data}</name>
        <__version__>vKMXGsXb7sEw42x2hnDqcf</__version__>
        <meta>
            <instanceID>uuid:{_uuid}</instanceID>
        </meta>
    </aK9ANfTMCGAQHNiunmQyki>
    '''
    return xml_data.encode()

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            _uuid = str(uuid.uuid4())
            data = name  # Change this to the data you want to submit
            file_tuple = (_uuid, io.BytesIO(create_xml_submission(data, _uuid)))
            files = {'xml_submission_file': file_tuple}
            headers = {'Authorization': f'Token {TOKEN}'}
            res = requests.post(SUMISSION_URL, files=files, headers=headers)

            if res.status_code == 201:
                message = 'Success 🎉'
            else:
                error = 'Something went wrong 😢'
                return render(request, 'home.html', {'error': error})

    else:
        form = MyForm()

    return render(request, 'home.html', {'form': form})


def todohome(request):
    kobo = Kobo.objects.all()
    form = KoboForm()

    if request.method == 'POST':
        form = KoboForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            'kobo': kobo,
            'form': form,}
            # Redirect after a successful POST to prevent form resubmission
            return render(request, 'todohome.html', context)  # Use the correct URL name


