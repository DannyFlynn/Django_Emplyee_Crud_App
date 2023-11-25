# Generated by Django 4.1.4 on 2023-11-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sick_days', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
                ('position', models.CharField(max_length=255)),
            ],
        ),
    ]