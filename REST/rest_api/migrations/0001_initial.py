# Generated by Django 4.0 on 2021-12-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProteinFamily',
            fields=[
                ('domain_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('domain_description', models.CharField(max_length=256)),
            ],
        ),
    ]
