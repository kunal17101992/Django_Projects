# Generated by Django 3.0 on 2020-06-27 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gender', models.CharField(max_length=100)),
                ('College_Name', models.CharField(blank=True, max_length=300, null=True)),
                ('School_Name', models.CharField(blank=True, max_length=300, null=True)),
                ('Marital_Status', models.CharField(blank=True, max_length=300, null=True)),
                ('Profession', models.CharField(blank=True, max_length=300, null=True)),
                ('Company', models.CharField(blank=True, max_length=300, null=True)),
                ('Location', models.CharField(blank=True, max_length=300, null=True)),
                ('Date_of_Birth', models.DateField()),
                ('Language_known', models.CharField(blank=True, max_length=300, null=True)),
                ('Religion', models.CharField(blank=True, max_length=300, null=True)),
                ('Contact_no', models.IntegerField(max_length=10)),
                ('Profile_photo', models.ImageField(blank=True, upload_to='profile_images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]