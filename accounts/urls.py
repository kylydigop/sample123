from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.loginPage.as_view(), name='login'),
    path('register/', views.registerPage.as_view(), name='register'),
    path('profile/', views.profilePage.as_view(), name='myProfile'),
    path('logout/', views.logoutUser, name='logout'),
]
