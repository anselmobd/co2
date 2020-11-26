# Generated by Django 3.1.3 on 2020-11-26 16:42

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201126_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('titulo_e_texto', wagtail.core.blocks.StructBlock([('titulo', wagtail.core.blocks.CharBlock(required=True)), ('texto', wagtail.core.blocks.TextBlock(help_text='Texto sem formatação', required=True))])), ('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock()), ('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))]))], blank=True, null=True),
        ),
    ]
