# Generated by Django 4.2 on 2023-07-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('edad', models.PositiveBigIntegerField()),
            ],
        ),
    ]
