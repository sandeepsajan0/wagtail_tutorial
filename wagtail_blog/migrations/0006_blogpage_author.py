# Generated by Django 3.0.3 on 2020-03-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_blog', '0005_blogtagindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author',
            field=models.CharField(default='sandeep', max_length=250),
        ),
    ]