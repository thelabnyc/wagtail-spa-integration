from django.urls import reverse
from django.test import override_settings
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.core.models import Page, Site
from wagtail.contrib.redirects.models import Redirect
from wagtail.tests.utils import WagtailPageTests
from rest_framework.test import APIRequestFactory
from .views import DraftPagesAPIEndpoint, RedirectViewSet


class CoreTests(WagtailPageTests):
    @override_settings(PREVIEW_DRAFT_CODE="abc")
    def test_draft_api(self):
        home = Page.objects.last()
        old_title = home.title
        new_title = 'edit it'
        home.title = new_title
        home.save_revision()

        request = APIRequestFactory().get("")
        request.site = Site.objects.first()
        request.wagtailapi_router = WagtailAPIRouter('wagtailapi')
        page_detail = DraftPagesAPIEndpoint.as_view({'get': 'detail_view'})
        res = page_detail(request, pk=home.pk)
        self.assertContains(res, old_title)
        self.assertNotContains(res, new_title)

        params = {'draft': 'abc'}
        request = APIRequestFactory().get("", params)
        request.site = Site.objects.first()
        request.wagtailapi_router = WagtailAPIRouter('wagtailapi')
        res = page_detail(request, pk=home.pk)
        self.assertContains(res, new_title)

    def test_redirect_viewset(self):
        params = {'old_path': '/lol/'}
        request = APIRequestFactory().get("", params)
        redirect_list = RedirectViewSet.as_view({'get': 'list'})
        Redirect.objects.create(old_path="/lol/", redirect_link="https://example.com")
        Redirect.objects.create(old_path="/test/", redirect_link="https://no.com")
        response = redirect_list(request)
        self.assertContains(response, "example.com")
        self.assertNotContains(response, "no.com")
