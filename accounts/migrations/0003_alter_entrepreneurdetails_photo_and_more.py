# Generated by Django 4.0.3 on 2023-11-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_investordetails_entrepreneurdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneurdetails',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/entrepreneur/'),
        ),
        migrations.AlterField(
            model_name='investordetails',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/investor/'),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/student/'),
        ),
    ]