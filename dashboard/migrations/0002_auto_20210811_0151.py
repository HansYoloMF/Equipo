# Generated by Django 3.2.6 on 2021-08-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doodle',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='to_do',
            name='due_date',
            field=models.DateField(),
        ),
    ]