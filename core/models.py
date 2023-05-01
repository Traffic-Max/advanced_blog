from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtailmetadata.models import MetadataPageMixin


class ExtPage(MetadataPageMixin, Page):
    keywords = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('meta keywords'),
    )

    search_fields = Page.search_fields + [
        index.SearchField('keywords', partial_match=True, boost=2),
    ]
    
    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),    
            FieldPanel('seo_title', heading=_('Title tag')),    
            FieldPanel('search_description'),    
            FieldPanel('keywords'),
            ImageChooserPanel('search_image'),    
        ], heading=_('For search engines')),
        MultiFieldPanel([
            FieldPanel('show_in_menus'),
        ], heading=_('For site menus')),
    ]
    
    settings_panels = Page.settings_panels
    
    class Meta:
        abstract = True
