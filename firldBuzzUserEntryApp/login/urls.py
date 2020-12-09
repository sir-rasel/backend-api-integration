from django.urls import path
from .views import HomeLoginView

urlpatterns = [
    path('', HomeLoginView.as_view(), name='login-page'),
]
