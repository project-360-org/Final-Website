# Generated by Django 3.2.12 on 2022-08-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_info',
            name='Video_link_7',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
