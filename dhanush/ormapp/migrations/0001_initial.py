# Generated by Django 5.1.2 on 2024-10-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('acc_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('ifsc_code', models.IntegerField()),
            ],
        ),
    ]
