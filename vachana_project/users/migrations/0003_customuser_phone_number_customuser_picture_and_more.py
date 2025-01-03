# Generated by Django 5.1.4 on 2024-12-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers_remove_customuser_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
