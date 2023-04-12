from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sign-up/", views.sign_up_view, name="sign-up"),
    path("sign-in/", views.sign_in_view, name="sign-in"),
    path("logout/", views.logout, name="logout"),
]
