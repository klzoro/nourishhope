# Generated by Django 5.1.6 on 2025-06-20 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0002_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('login_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donate.login')),
            ],
        ),
    ]
