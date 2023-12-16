from django.urls import path

from .views import register, loginpage, logout_view, dashboard

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginpage, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]