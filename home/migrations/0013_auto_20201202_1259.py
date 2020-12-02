# Generated by Django 3.1.3 on 2020-12-02 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0012_homepagecarouselimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagem do banner'),
        ),
        migrations.AlterField(
            model_name='homepagecarouselimages',
            name='carousel_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagem'),
        ),
    ]
