# Generated by Django 3.1.6 on 2021-02-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions_and_points', '0003_auto_20210208_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payer',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]