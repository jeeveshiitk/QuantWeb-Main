# Generated by Django 5.0.6 on 2024-06-20 09:44

import python_field.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', python_field.fields.PythonCodeField(blank=True, null=True)),
            ],
        ),
    ]