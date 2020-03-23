from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.snippets.models import register_snippet
from .blocks import LinkChildrenBlock

# Create your models here


@register_snippet
class Navbar(models.Model):
    """
    Model that represents website navigation bars.  Can be modified through the
    snippets UI.
    """
    name = models.CharField(max_length=255)
    menu_items = StreamField([
        ('menu', blocks.StructBlock([
            ("name", blocks.CharBlock()),
            ('external_link', LinkChildrenBlock()),
            ],
        template="menu.html"),),
        ],)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('menu_items')
    ]

    def __str__(self):
        return self.name


class ServicesNavbar(Page):
    navbar = models.ForeignKey(
        Navbar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    premium_service = StreamField([
        ('service', blocks.StructBlock([
            ("icon", ImageChooserBlock()),
            ("service_name", blocks.CharBlock()),
            ("intro", blocks.CharBlock(required=False)),
            ("return", blocks.CharBlock(required=False)),
            ("sip", blocks.CharBlock(required=False) ),
            ("return_intro", blocks.CharBlock(required=False)),
            ("features_list", blocks.ListBlock(blocks.StructBlock([
                ("feature_heading", blocks.CharBlock(required=False)),
                ("feature_intro", blocks.CharBlock(required=False))
            ],
            template = "features_list.html"))),
            ("price", blocks.CharBlock(required=False)),
            ("status", blocks.ChoiceBlock(choices=[
                ('open', 'open'),
                ('closed', 'closed'),
            ], required=False)),
            ("image_heading", blocks.CharBlock(required=False)),
            ("image_intro", blocks.CharBlock(required=False)),
            ("image", ImageChooserBlock(required=False)),
            ],
        template= "service.html" ),
        ),
    ], null = True)

    content_panels=[
        FieldPanel('title'),
        SnippetChooserPanel('navbar'),
        StreamFieldPanel("premium_service"),
    ]

