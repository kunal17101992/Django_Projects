# Generated by Django 3.0 on 2020-06-29 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, upload_to='postimages/')),
                ('Video', models.FileField(blank=True, upload_to='videos/')),
                ('file', models.FileField(blank=True, upload_to='files/')),
                ('Published_date', models.DateField(default=django.utils.timezone.now)),
                ('postuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
