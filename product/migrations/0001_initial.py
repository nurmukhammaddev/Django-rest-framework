# Generated by Django 4.1.1 on 2022-10-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=211)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
