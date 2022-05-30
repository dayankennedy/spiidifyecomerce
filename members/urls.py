from django.urls import path
from  .import views



urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('loginPage/',views.loginPage, name='login'),
    path('logoutPage/', views.logoutPage, name='logout'),
]

