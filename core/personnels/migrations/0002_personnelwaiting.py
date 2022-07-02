# Generated by Django 3.2 on 2022-07-01 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0007_delete_barberdata'),
        ('personnels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonnelWaiting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_date', models.DateField()),
                ('barber_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbers.barber')),
                ('personnel_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnels.personnel')),
            ],
            options={
                'ordering': ['-reserved_date'],
            },
        ),
    ]