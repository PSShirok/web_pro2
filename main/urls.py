from django.urls import path

from main.views import contacts_index, home_index

urlpatterns = [
    path('', contacts_index),
    path('', home_index)
]
