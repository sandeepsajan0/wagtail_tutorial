# Generated by Django 3.0.3 on 2020-03-22 12:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_auto_20200322_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesnavbar',
            name='premium_service',
            field=wagtail.core.fields.StreamField([('service', wagtail.core.blocks.StructBlock([('service_name', wagtail.core.blocks.CharBlock()), ('return', wagtail.core.blocks.CharBlock()), ('S&P', wagtail.core.blocks.CharBlock()), ('intro', wagtail.core.blocks.CharBlock())]))], null=True),
        ),
    ]
