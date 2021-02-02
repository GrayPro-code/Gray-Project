# Generated by Django 3.1.4 on 2021-01-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_image', models.ImageField(upload_to='post_images/')),
                ('site_title', models.CharField(max_length=300)),
                ('site_text', models.TextField()),
                ('site_link', models.TextField()),
            ],
        ),
    ]
