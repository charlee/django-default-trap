# Generated by Django 2.0.5 on 2018-05-08 23:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('detail', django.contrib.postgres.fields.jsonb.JSONField(default={}, editable=False)),
            ],
        ),
    ]
