from django.shortcuts import render, redirect
from django.views import View
from .loginForm import LoginForm
import requests
import json

class HomeLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login/loginPage.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            userName = form.cleaned_data['userName']
            password = form.cleaned_data['password']
            credentials = {'username':f'{userName}', 'password':f'{password}'}

            loginApiUrl = 'https://recruitment.fisdev.com/api/login/'
            response = requests.post(loginApiUrl, json=credentials)

            if response.status_code == 200:
                token = json.loads(response.text)['token']
                return redirect(f'/user/{token}')
            else:
                return redirect('login-page')