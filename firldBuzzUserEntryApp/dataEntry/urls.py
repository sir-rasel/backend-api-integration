from django.urls import path
from .views import UserDataEntryView

urlpatterns = [
    path('', UserDataEntryView.as_view(), name='user-data-entry-page'),
]
