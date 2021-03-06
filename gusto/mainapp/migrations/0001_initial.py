# Generated by Django 4.0.5 on 2022-06-05 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('image', models.CharField(max_length=255, verbose_name='фото')),
                ('price', models.PositiveIntegerField(verbose_name='цена')),
                ('description', models.TextField(verbose_name='описание')),
                ('calories', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='калории')),
                ('type', models.CharField(choices=[('FS', 'Первое'), ('SC', 'Второе'), ('DR', 'Питье')], default=('FS', 'Первое'), max_length=2, verbose_name='тип еды')),
            ],
        ),
    ]
