# Generated by Django 3.2.5 on 2021-08-30 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='videos',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videos',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='videos',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='videos',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='videoapp.videos')),
            ],
        ),
    ]
