# Generated by Django 3.1.3 on 2020-11-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('newsHeading', models.CharField(max_length=500)),
                ('newsContent', models.CharField(max_length=10000)),
            ],
        ),
    ]