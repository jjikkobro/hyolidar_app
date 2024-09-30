# accounts/views.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView

app_name="common"

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name = "common/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
]