# Generated by Django 5.1.3 on 2024-12-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('task_type', models.CharField(choices=[('work', 'Work'), ('exercise', 'Exercise'), ('household', 'Household'), ('leisure', 'Leisure')], max_length=50)),
                ('frequency', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=50)),
                ('duration', models.IntegerField()),
                ('priority', models.CharField(choices=[('medium', 'Medium'), ('low', 'Low')], max_length=50)),
                ('physical_effort', models.CharField(choices=[('light', 'Light'), ('moderate', 'Moderate'), ('intense', 'Intense')], max_length=50)),
                ('tiredness_factor', models.IntegerField()),
            ],
        ),
    ]
