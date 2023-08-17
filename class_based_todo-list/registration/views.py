from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

# Create your views here.
class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('todo-list')

    def form_valid(self,form):
        response=super().form_valid(form)
        login(self.request,self.object)
        return response
    
class UserLoginView(LoginView):
    template_name='registration/login.html'
    success_url=reverse_lazy('todo-list')
    authentication_form = AuthenticationForm

class UserLogoutView(LogoutView):
    next_page=''



