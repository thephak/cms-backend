# Generated by Django 3.2.8 on 2021-10-08 11:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Title')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Published Date')),
                ('author', models.CharField(blank=True, max_length=200, verbose_name='Author')),
                ('summary', models.TextField(blank=True, verbose_name='Summary')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=30, verbose_name='Status')),
            ],
        ),
    ]
