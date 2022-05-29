from django.urls import path
from  .import views



urlpatterns = [
    path('members/',views.signup, name='signup'),
    path('', views.signup, name='signup'),
    path('loginPage/', views.loginPage, name='login'),
    path('logoutPage/', views.logoutPage, name='logout'),
]

