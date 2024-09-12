from django.db import models
from django.utils import timezone


class Week(models.Model):
    start_date = models.DateField(verbose_name='Дата начала недели')

    def __str__(self):
        return f"Неделя {self.start_date.strftime('%d.%m.%Y')}"


class Day(models.Model):
    week = models.ForeignKey(Week, related_name='days', on_delete=models.CASCADE, verbose_name='Неделя')
    date = models.DateField(verbose_name='Дата', default=timezone.now)

    DAYS_OF_WEEK = [
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
    ]

    def get_day_name(self):
        return self.DAYS_OF_WEEK[self.date.weekday()][1]

    def __str__(self):
        return f"{self.get_day_name()} - {self.date.strftime('%d.%m.%Y')}"


class HomeTask(models.Model):
    day = models.ForeignKey(Day, related_name='hometasks', on_delete=models.CASCADE, verbose_name='День')
    SUBJECT_CHOICES = [
        ('ENG', 'Английский язык'),
        ('RUS', 'Русский язык'),
        ('ALG', 'Алгебра'),
        # другие предметы
    ]
    subject = models.CharField(max_length=3, choices=SUBJECT_CHOICES, verbose_name='Предмет')
    task_text = models.TextField(max_length=256, verbose_name='Текст задания')
    assigned_date = models.DateField(auto_now_add=True, verbose_name='Дата задания')
    STATUS_CHOICES = [
        ('RES', 'Решено'),
        ('NOT', 'Нерешено'),
        ('URG', 'СРОЧНО'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='NOT', verbose_name='Статус', blank=True, null=True)
    due_date = models.DateField(null=True, blank=True, verbose_name="Срок сдачи")

    def __str__(self):
        return f"{self.subject} - {self.task_text[:20]}"

    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, 'Неизвестно')

    def get_subject_display(self):
        return dict(self.SUBJECT_CHOICES).get(self.subject, 'Неизвестно')

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = 'NOT'
        super().save(*args, **kwargs)
