# Generated by Django 4.2.4 on 2023-12-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperationrequest',
            name='date_brd',
            field=models.CharField(max_length=40),
        ),
    ]