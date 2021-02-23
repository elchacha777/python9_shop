from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import RegistrationView, ActivationView, SigningView, SuccessfullyRegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('successfully_registration/', SuccessfullyRegistrationView.as_view(), name='successfully_registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login/', SigningView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]