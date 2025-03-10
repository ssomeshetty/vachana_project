# Generated by Django 5.1.4 on 2024-12-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('information', models.TextField(verbose_name='Author Information')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='authors_photos/')),
            ],
        ),
    ]
