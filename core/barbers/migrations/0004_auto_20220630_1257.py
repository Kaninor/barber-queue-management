# Generated by Django 3.2 on 2022-06-30 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0003_remove_barber_earned_money'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barber',
            name='number_of_hair_cut',
        ),
        migrations.CreateModel(
            name='BarberData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_hair_cut', models.IntegerField()),
                ('barber_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbers.barber')),
            ],
        ),
    ]
