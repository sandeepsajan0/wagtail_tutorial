# Generated by Django 3.0.3 on 2020-03-22 11:55

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20200322_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='menu_items',
            field=wagtail.core.fields.StreamField([('external_link', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('children', wagtail.core.blocks.StreamBlock([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock())])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock()), ('page', wagtail.core.blocks.PageChooserBlock())]))]))]))]),
        ),
    ]
