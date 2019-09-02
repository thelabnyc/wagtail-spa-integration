from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.core.models import Page


class FooPage(Page):
    body = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]
    api_fields = [APIField('body')]


class BarPage(Page):
    pass
