from django import template
from django.conf import settings

from ..utils import hash_draft_code

register = template.Library()


@register.simple_tag(takes_context=True)
def get_preview_code(context: template.Context) -> str:
    assert hasattr(context, "request")
    page_id = context.request.resolver_match.kwargs["page_id"]
    return hash_draft_code(settings.PREVIEW_DRAFT_CODE, int(page_id))
