from django.urls import path

from .views import (home,
                    about, cause_create, cause_delete, cause_detail, cause_edit, donation_create, causes_list
                    )

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('causes/', causes_list, name='causes_list'),
    path('causes/<int:pk>/', cause_detail, name='cause_detail'),
    path('causes/new/', cause_create, name='cause_create'),
    path('causes/<int:pk>/edit/', cause_edit, name='cause_edit'),
    path('causes/<int:pk>/delete/', cause_delete, name='cause_delete'),
    path('causes/<int:pk>/donations/new/', donation_create, name='donation_create'),
]

