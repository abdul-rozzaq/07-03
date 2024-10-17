# Generated by Django 5.1.2 on 2024-10-17 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_submission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='project.assignment'),
        ),
    ]
