# Generated by Django 2.0.8 on 2019-06-30 13:34

from django.db import migrations, models
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', upload_to=userprofile.models.upload_to),
        ),
    ]
