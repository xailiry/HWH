from django.urls import path

from .views import *


urlpatterns = [
    path('week/<int:week_id>/', week_detail, name='week_detail'),
    path('create/', create_hometask, name='create_hometask')
]
