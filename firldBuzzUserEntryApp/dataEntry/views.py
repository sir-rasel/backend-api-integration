from django.shortcuts import render, redirect
from django.views import View
from .userDataForm import UserDataForm
import uuid
import time
import requests
import json

class UserDataEntryView(View):
    def get(self, request, token=None):
        if token : 
            form = UserDataForm()
            return render(request, 'dataEntry/userInfoPage.html', {'form':form, 'token':token})
        else:
            return redirect('login-page')

    def post(self, request, token):
        form = UserDataForm(request.POST, request.FILES)
        
        if form.is_valid():
            testSubmitUrl = "https://recruitment.fisdev.com/api/v0/recruiting-entities/"
            # finalSubmitUrl = "https://recruitment.fisdev.com/api/v1/recruiting-entities/"

            dataInstanceCreateTime = int(round(time.time() * 1000))

            userData = {
                "tsync_id": str(uuid.uuid4()),
                "name": form.cleaned_data['userName'],
                "email": form.cleaned_data['email'],
                "phone": form.cleaned_data['phone'],
                "full_address": form.cleaned_data['address'],
                "name_of_university": form.cleaned_data['university'],
                "graduation_year": form.cleaned_data['graduationYear'],
                "cgpa": float(form.cleaned_data['cgpa']),
                "experience_in_months": form.cleaned_data['experience'],
                "current_work_place_name": form.cleaned_data['workPlace'],
                "applying_in": form.cleaned_data['applyingIn'],
                "expected_salary": form.cleaned_data['salary'],
                "field_buzz_reference": form.cleaned_data['refference'],
                "github_project_url": form.cleaned_data['projectUrl'],
                "cv_file": {
                    "tsync_id": str(uuid.uuid4()),
                },
                "on_spot_update_time": dataInstanceCreateTime,
                 "on_spot_creation_time": dataInstanceCreateTime
            }

            headers={'Authorization': f'token {token}'}
            response = requests.post(testSubmitUrl, json=userData, headers=headers)

            if response.status_code == 201:
                fileTokenId = json.loads(response.text)['cv_file']['id']
                fileSubmitUrl = f'https://recruitment.fisdev.com/api/file-object/{fileTokenId}/'

                cvFile = {'file' : request.FILES['cvFile']}
                headers['Content_type'] = 'application/pdf'
                response = requests.post(fileSubmitUrl, files=cvFile, headers=headers)
                
                if response.status_code == 200:
                    return render(request, 'dataEntry/massage.html', {'massage':"Successfully Posted data via api request"})
                else:
                    return render(request, 'dataEntry/massage.html', {'massage':"Successfully Created data But failed to submit CV file"})
            else:
                return render(request, 'dataEntry/massage.html', {'massage':'Error to create data via api request'})
        else:
            return render(request, 'dataEntry/massage.html', {'massage':form.errors})