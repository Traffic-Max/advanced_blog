# Generated by Django 4.1.8 on 2023-05-01 19:59

from django.db import migrations, models
import django.db.models.deletion
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='meta keywords')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]