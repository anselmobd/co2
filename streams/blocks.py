"""Streamfields live in here."""

from wagtail.core import blocks


class TituloETextoBlock(blocks.StructBlock):
    """Título e Texto e nada mais."""

    titulo = blocks.CharBlock(required=True)
    texto = blocks.TextBlock(required=True, help_text="Texto sem formatação")

    class Meta:
        template = "streams/titulo_e_texto_block.html"
        icon = "edit"
        label = "Título & Texto"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "RichText completo"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
        self, required=True, help_text=None, editor="default",
        features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"
