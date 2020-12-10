from django.urls import path, include
from django.shortcuts import redirect
from .views import UserDataEntryView

urlpatterns = [
    path('', UserDataEntryView.as_view()),
    path('<str:token>', UserDataEntryView.as_view(), name='user-data-entry-page'),
]
