from django.db import models


class Hometask(models.Model):
    # предмет с выбором конкретных предметов
    SUBJECT_CHOICES = [
        ('ENG', 'Английский язык'),
        ('RUS', 'Русский язык'),
        ('ALG', 'Алгебра'),
        ('GEO', 'Геометрия'),
        ('GRH', 'География'),
        ('PEC', 'Физкультура'),
        ('HIM', 'Химия'),
        ('OBZ', 'ОБЖ'),
        ('BIO', 'Биология'),
        ('PHS', 'Физика'),
        ('INF', 'Информатика'),
        ('LIT', 'Литература'),
        ('IST', 'История'),
        ('TRD', 'Труды'),
        # и д.р...
    ]
    subject = models.CharField(max_length=3, choices=SUBJECT_CHOICES, verbose_name="Предмет")

    # дата, когда задали (устанавливается автоматически на текущую дату)
    assigned_date = models.DateField(auto_now_add=True, verbose_name="Дата задания")

    # cтепень решенности
    STATUS_CHOICES = [
        ('RES', 'Решено'),
        ('NOT', 'Нерешено'),
        ('URG', 'СРОЧНО'),
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='NOT', verbose_name="Статус")

    # текст домашнего задания
    task_text = models.TextField(verbose_name="Текст задания")

    # дата, до которой задание должно быть выполнено (сроки)
    due_date = models.DateField(verbose_name="Срок выполнения")

    def __str__(self):
        return f"{self.get_subject_display()} - {self.task_text[:20]}"
