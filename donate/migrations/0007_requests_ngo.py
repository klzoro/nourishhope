# Generated by Django 5.1.6 on 2025-06-25 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_rename_name_requests_food'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='ngo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donate.login'),
        ),
    ]
