# Generated by Django 3.2.5 on 2022-05-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20220510_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='desciption',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]
