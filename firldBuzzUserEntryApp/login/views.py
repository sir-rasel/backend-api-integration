from django.shortcuts import render, redirect
from django.views import View

class HomeLoginView(View):
    def get(self, request):
        return render(request, 'login/loginPage.html')
