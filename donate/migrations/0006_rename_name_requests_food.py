# Generated by Django 5.1.6 on 2025-06-25 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0005_requests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='name',
            new_name='food',
        ),
    ]
