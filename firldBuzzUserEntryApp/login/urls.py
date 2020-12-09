from django.urls import path
from .views import loginView

urlpatterns = [
    path('', loginView.as_view(), name='login-page'),
]
