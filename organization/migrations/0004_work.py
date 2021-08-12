# Generated by Django 3.2.6 on 2021-08-12 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0003_alter_organization_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('files', models.FileField(blank=True, null=True, upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('is_complete', models.BooleanField()),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='work', to='organization.member')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigner', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='organization.organization')),
            ],
            options={
                'ordering': ['-created_on', 'is_complete'],
            },
        ),
    ]
