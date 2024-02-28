from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Create your views here.
class Login(LoginView):
    template_name = 'accounts/login.html'
    fields = "username","password"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("task_list")


    
   
class RegisterPage(FormView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = '/tasks/'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task_list")
        return super(RegisterPage, self).get(*args, **kwargs)