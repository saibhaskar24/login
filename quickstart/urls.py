from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views


urlpatterns = [
	path('', views.index, name = 'index'),
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='quickstart/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='quickstart/logout.html'), name='logout'),
]