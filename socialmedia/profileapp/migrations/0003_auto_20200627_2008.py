# Generated by Django 3.0 on 2020-06-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_auto_20200627_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Contact_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Date_of_Birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
