from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("view/", views.view_feedback, name="view_feedback"),
    path("send/", views.send_feedback, name="send_feedback"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path('register/', views.register_user, name="register"),
]
