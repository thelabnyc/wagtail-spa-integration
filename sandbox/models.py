from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.core.models import Page
from wagtail_headless_preview.models import HeadlessPreviewMixin


class FooPage(HeadlessPreviewMixin, Page):
    body = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]
    api_fields = [APIField('body')]


class BarPage(HeadlessPreviewMixin, Page):
    pass
