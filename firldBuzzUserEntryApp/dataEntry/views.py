from django.shortcuts import render
from django.views import View

class UserDataEntryView(View):
    def get(self, request):
        return render(request, 'dataEntry/userInfoPage.html')

