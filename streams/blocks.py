"""Streamfields live in here."""

from wagtail.core import blocks


class TituloETextoBlock(blocks.StructBlock):
    """Título e Texto e nada mais."""

    titulo = blocks.CharBlock(required=True)
    texto = blocks.TextBlock(required=True, help_text="Texto sem formatação")

    class Meta:  # noqa
        template = "streams/titulo_e_texto_block.html"
        icon = "edit"
        label = "Título & Texto"
