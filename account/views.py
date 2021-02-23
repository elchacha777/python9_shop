from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.views.generic.base import View

from account.forms import RegistrationForm

User = get_user_model()

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('successfully_registration')

class SuccessfullyRegistrationView(View):
    def get(self, request):
        return render(request, 'account/successfully_registration.html', {})


#Создаем пользователя

class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User,  activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html', {})




class SigningView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index-page')



class ForgotPassword():
    pass


class ChangePassword():
    pass
