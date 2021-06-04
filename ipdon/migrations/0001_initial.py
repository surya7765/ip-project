# Generated by Django 3.2.4 on 2021-06-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('prize', models.IntegerField()),
                ('contest_url', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=200)),
                ('event_name', models.CharField(max_length=20)),
                ('event_desc', models.CharField(max_length=500)),
            ],
        ),
    ]