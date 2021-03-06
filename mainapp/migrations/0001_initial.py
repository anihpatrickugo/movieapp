# Generated by Django 3.2.5 on 2022-05-09 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TvShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250)),
                ('cover_photo', models.ImageField(upload_to='movie_covers/')),
                ('upload_date', models.DateField(auto_now=True)),
                ('genre', models.ManyToManyField(to='mainapp.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250)),
                ('cover_photo', models.ImageField(upload_to='movie_covers/')),
                ('video', models.FileField(upload_to='movie_covers/')),
                ('upload_date', models.DateField(auto_now=True)),
                ('genre', models.ManyToManyField(to='mainapp.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('tvshow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tvshow')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250)),
                ('cover_photo', models.ImageField(upload_to='movie_covers/')),
                ('video', models.FileField(upload_to='movie_covers/')),
                ('upload_date', models.DateField(auto_now=True)),
                ('genre', models.ManyToManyField(to='mainapp.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('video', models.FileField(upload_to='movie_videos/')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.season')),
            ],
        ),
    ]
