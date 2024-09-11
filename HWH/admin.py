from django.contrib import admin

from .models import Week, Day, HomeTask


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('start_date', "id")
    ordering = ('start_date',)
    search_fields = ('start_date',)


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('date', 'week', 'get_day_name', 'id')
    ordering = ('date',)
    search_fields = ('date', 'week__start_date')


@admin.register(HomeTask)
class HomeTaskAdmin(admin.ModelAdmin):
    list_display = ('subject', 'task_text', 'status', 'day', 'due_date')
    ordering = ('day', 'due_date')
    search_fields = ('subject', 'task_text')
    list_filter = ('status', 'due_date', 'day__date')
