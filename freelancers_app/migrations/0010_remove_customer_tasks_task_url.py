# Generated by Django 5.0.2 on 2024-11-28 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers_app', '0009_alter_taskapplication_freelancer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_tasks',
            name='task_url',
        ),
    ]
