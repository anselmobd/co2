# Generated by Django 3.1.3 on 2020-11-30 12:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('home', '0007_pricipalpage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PricipalPage',
            new_name='PrincipalPage',
        ),
    ]
