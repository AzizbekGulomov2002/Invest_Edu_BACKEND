# Generated by Django 4.0.1 on 2022-05-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menyu_fanlar',
            name='rasm',
            field=models.ImageField(null=True, upload_to='rasmlar/%Y/%m/%d'),
        ),
    ]
