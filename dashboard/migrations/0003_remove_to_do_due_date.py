# Generated by Django 3.2.6 on 2021-08-10 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20210811_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='to_do',
            name='due_date',
        ),
    ]