from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CreateUser, LoginUser
from django.urls import reverse_lazy

# Create your views here.

class LoginUser(LoginView):
    template_name = 'userAuth/login.html'
    form_class = LoginUser

class LogOutUser(LogoutView):
    template_name = 'userAuth/logout.html'
    
    


    

class Register(CreateView):
    template_name =  'userAuth/signup.html'
    form_class = CreateUser
    success_url = reverse_lazy('login')
   

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)
