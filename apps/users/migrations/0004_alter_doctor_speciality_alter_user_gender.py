# Generated by Django 5.0.6 on 2024-07-10 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('internal_medicine', 'терапевт'), ('pediatrics', 'педиатр'), ('surgery', 'хирург'), ('cardiology', 'кардиолог'), ('neurology', 'невролог'), ('ophthalmology', 'офтальмолог')], max_length=150, verbose_name='специальность'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'мужчина'), ('female', 'женщина'), ('other', 'другое')], max_length=15, verbose_name='пол'),
        ),
    ]