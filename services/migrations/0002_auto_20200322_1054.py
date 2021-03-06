# Generated by Django 3.0.3 on 2020-03-22 10:54

from django.conf import settings
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PageWithNavbar',
            new_name='ServicesNavbar',
        ),
        migrations.AlterField(
            model_name='navbar',
            name='menu_items',
            field=wagtail.core.fields.StreamField([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock())])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock()), ('page', wagtail.core.blocks.PageChooserBlock())]))]),
        ),
    ]
