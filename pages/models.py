from core.models import ExtPage

from django.db import models



class HomePage(ExtPage):
    object_type = 'website'
    schemaorg_type = 'website'
    
