# Generated by Django 5.0.6 on 2024-06-01 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('madhavapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultimage',
            old_name='enroll_number',
            new_name='roll_number',
        ),
    ]
