# Generated by Django 4.1.3 on 2022-11-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirdropModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('frequency', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('once', 'Once')], max_length=10)),
                ('wallet', models.CharField(max_length=255)),
                ('network', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('endDate', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('walletCode', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=11)),
                ('message', models.TextField()),
            ],
        ),
    ]
