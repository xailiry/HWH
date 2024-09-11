import datetime

from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from .forms import HometaskForm
from .models import Week, Day


def create_hometask(request):
    if request.method == 'POST':
        form = HometaskForm(request.POST)
        if form.is_valid():
            hometask = form.save(commit=False)

            # Определяем текущую дату
            current_date = timezone.now().date()

            # Находим или создаем неделю
            start_of_week = current_date - datetime.timedelta(days=current_date.weekday())  # понедельник
            week, created = Week.objects.get_or_create(start_date=start_of_week)

            # Находим или создаем день
            day, created = Day.objects.get_or_create(week=week, date=current_date)

            # Связываем домашнее задание с днем
            hometask.day = day
            hometask.save()

            return redirect('week_detail', week_id=week.id)  # редирект на список ДЗ

    else:
        form = HometaskForm()

    return render(request, 'HWH/create_hometask.html', {'form': form})


# def week_detail(request, week_id):
#     # Получаем неделю по её ID
#     week = get_object_or_404(Week, id=week_id)
#
#     # Передаем неделю в шаблон
#     return render(request, 'HWH/hometask-list.html', {'week': week})
#

class WeekListView(ListView):
    model = Week
    template_name = 'HWH/hometask-list.html'  # Шаблон, где будет отображаться список недель
    context_object_name = 'weeks'
    paginate_by = 1  # Пагинация: одна неделя на одну страницу


def day_detail_view(request, week_id, day_id):
    week = Week.objects.get(pk=week_id)
    day = Day.objects.get(pk=day_id, week=week)
    return render(request, 'HWH/day-detail.html', {'week': week, 'day': day})
