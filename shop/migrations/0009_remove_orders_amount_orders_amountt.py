# Generated by Django 4.1.3 on 2022-12-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orders_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
        migrations.AddField(
            model_name='orders',
            name='amountt',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
