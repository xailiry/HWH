# Generated by Django 5.1.1 on 2024-09-08 15:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала недели')),
            ],
        ),
        migrations.CreateModel(
            name='HomeTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('ENG', 'Английский язык'), ('RUS', 'Русский язык'), ('ALG', 'Алгебра')], max_length=3, verbose_name='Предмет')),
                ('task_text', models.TextField(verbose_name='Текст задания')),
                ('assigned_date', models.DateField(auto_now_add=True, verbose_name='Дата задания')),
                ('status', models.CharField(choices=[('RES', 'Решено'), ('NOT', 'Нерешено'), ('URG', 'СРОЧНО')], default='NOT', max_length=3, verbose_name='Статус')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hometasks', to='HWH.day', verbose_name='День')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='HWH.week', verbose_name='Неделя'),
        ),
    ]
