# Generated by Django 3.0.5 on 2020-04-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('book_ref', models.AutoField(primary_key=True, serialize=False)),
                ('book_date', models.DateField(auto_now_add=True)),
                ('total_amount', models.FloatField()),
            ],
        ),
    ]
