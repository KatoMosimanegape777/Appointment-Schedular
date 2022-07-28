from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='index.html'), name="home"),
    path('logout/', views.logout_view, name='logout'),
]