# Generated by Django 5.0.2 on 2024-11-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancers_app', '0011_freelancerprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='payment_amount',
            field=models.CharField(blank=True, null=True),
        ),
    ]
