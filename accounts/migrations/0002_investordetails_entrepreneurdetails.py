# Generated by Django 4.0.3 on 2023-11-07 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=12)),
                ('landline_number', models.CharField(blank=True, max_length=12)),
                ('website', models.URLField(blank=True, default='')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('about', models.TextField()),
                ('focus_industries', models.CharField(max_length=100)),
                ('focus_sectors', models.CharField(max_length=100)),
                ('startup_stages', models.CharField(max_length=100)),
                ('min_investment_range', models.IntegerField()),
                ('max_investment_range', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'InvestorDetails',
            },
        ),
        migrations.CreateModel(
            name='EntrepreneurDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('interest1', models.CharField(max_length=100)),
                ('interest2', models.CharField(max_length=100)),
                ('interest3', models.CharField(max_length=100)),
                ('about_yourself', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
