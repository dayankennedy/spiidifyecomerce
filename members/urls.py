from django.urls import path
from  .import views



urlpatterns = [
    path('members/',views.signup, name='signup'),
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

