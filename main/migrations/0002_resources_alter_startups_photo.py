# Generated by Django 4.0.3 on 2023-10-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/resources/%Y/%m/%d/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=512)),
                ('modules', models.IntegerField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='startups',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/startups/%Y/%m/%d/'),
        ),
    ]
