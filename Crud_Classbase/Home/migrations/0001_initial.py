# Generated by Django 4.0.2 on 2024-05-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data1', models.CharField(max_length=50)),
                ('data2', models.CharField(max_length=50)),
            ],
        ),
    ]
