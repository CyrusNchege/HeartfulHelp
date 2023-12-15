from django.urls import path

from .views import register, loginpage, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginpage, name='login'),
    path('logout/', logout_view, name='logout'),
]