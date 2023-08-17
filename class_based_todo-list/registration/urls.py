from django.urls import path
from .views import UserRegistrationView , UserLoginView,UserLogoutView

urlpatterns=[
    path('',UserLoginView.as_view(),name='login'),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    
]