# Generated by Django 4.0.3 on 2023-11-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_entrepreneurdetails_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=200)),
                ('sector', models.CharField(max_length=100)),
                ('business_phone_number', models.CharField(max_length=15)),
                ('document1', models.FileField(upload_to='%Y/%m/%d/files/ProjectDoc1/')),
                ('document2', models.FileField(blank=True, upload_to='%Y/%m/%d/files/ProjectDoc2/')),
                ('theme', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=10)),
                ('problem_statement_title', models.TextField()),
                ('problem_statement_description', models.TextField()),
                ('demo_link', models.URLField(blank=True, null=True)),
                ('dataset', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterField(
            model_name='entrepreneurdetails',
            name='photo',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d/photos/entrepreneur/'),
        ),
        migrations.AlterField(
            model_name='investordetails',
            name='photo',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d/photos/investor/'),
        ),
    ]
