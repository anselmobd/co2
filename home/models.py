from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

import streams.blocks


class PrincipalPage(Page):
    """Página principal oficial"""
    max_count = 1

    texto = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('texto'),
    ]


class LinksPage(Page):
    """Página de links"""

    texto = RichTextField(blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('texto'),
    ]


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [ImageChooserPanel("carousel_image")]


class HomePage(Page):
    """Modelo de página principal"""
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    body = RichTextField(blank=True)

    content = StreamField(
        [
            ("cta", streams.blocks.CTABlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        ImageChooserPanel('banner_image'),
        PageChooserPanel('banner_cta'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel("content"),
        InlinePanel("carousel_images", max_num=5, min_num=1, label="Imagem"),
    ]

    class Meta:
        verbose_name = 'Página principal'
        verbose_name_plural = 'Páginas principais'
