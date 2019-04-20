from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect
from django_filters import rest_framework as filters
from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.utils import BadRequestError
from wagtail.contrib.redirects.models import Redirect
from wagtail.core.models import Site
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import RedirectSerializer


class DraftPagesAPIEndpoint(PagesAPIEndpoint):
    """
    Wagtail preview doesn't work with a JS client
    This tweaked Pages API will serve the latest draft version of a page when
    ?draft=[draft_code] is set.
    """
    known_query_parameters = PagesAPIEndpoint.known_query_parameters.union([
        'site',
    ])

    def detail_view(self, request, pk):
        instance = self.get_object()
        draft_code = getattr(settings, 'PREVIEW_DRAFT_CODE', None)
        if draft_code and request.GET.get('draft') == draft_code:
            instance = instance.get_latest_revision_as_page()
        elif not instance.live:
            raise Http404
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def find_view(self, request):
        """
        Override to append preview GET param to redirect url
        """
        url = super().find_view(request).url
        draft_code = request.GET.get('draft')
        draft_code = getattr(settings, 'PREVIEW_DRAFT_CODE', None)
        if draft_code and request.GET.get('draft') == draft_code:
            url += f"?draft={draft_code}"
        return redirect(url)

    def get_queryset(self):
        site_id = self.request.GET.get('site', None)
        if site_id:
            try:
                self.request.site = Site.objects.get(id=site_id)
            except Site.DoesNotExist:
                raise BadRequestError("Site not found")
        queryset = super().get_queryset()
        return queryset
        


class RedirectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('old_path', 'site')
