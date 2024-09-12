from django.urls import path

from .views import *

urlpatterns = [
    path('', WeekListView.as_view(), name='week_list'),  # Главная страница с пагинацией по неделям
    path('create/', create_hometask, name='create_hometask'),
    path('<int:week_id>/<int:day_id>/',  day_detail_view, name='day_detail'),
    path('all/', all_hw_list, name='all_hw_list')
]
