# Generated by Django 3.0 on 2020-06-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0004_auto_20200627_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Profile_photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_images/'),
        ),
    ]