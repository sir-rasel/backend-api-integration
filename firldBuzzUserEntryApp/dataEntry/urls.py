from django.urls import path
from .views import userDataEntryView

urlpatterns = [
    path('user/', userDataEntryView.as_view(), name='user-data-entry-page'),
]
