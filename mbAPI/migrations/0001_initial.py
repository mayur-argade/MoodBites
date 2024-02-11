# Generated by Django 5.0.1 on 2024-02-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('rest_type', models.CharField(max_length=255)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('votes', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]
