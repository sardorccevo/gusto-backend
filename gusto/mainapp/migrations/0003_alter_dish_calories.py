# Generated by Django 4.0.5 on 2022-06-05 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_dish_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='calories',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='калории'),
        ),
    ]
