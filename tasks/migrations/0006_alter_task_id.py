# Generated by Django 5.1.3 on 2025-01-08 18:35

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
