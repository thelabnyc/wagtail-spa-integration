# Wagtail Single Page Application Integration

This project provides some tools for using Wagtail as an API only CMS that a JS application will consume.

It was designed to work with angular-wagtail - but works without Angular if you provide the client integration.

## Features

- Wagtail Redirect API
- Preview button support thanks to wagtail-headless-preview
- Get page detail view by html_path (faster than find_view's redirect and more compatible with non-browser platforms)
- Exclude pages by explicit site and/or page type
- Supports multiple wagtail sites
  - Adds explicit site query parameter to wagtail sitemap.xml function
- Only adds features, does not break compatibility with Wagtail V2 Pages Endpoint
- Nothing in this package is Angular specific, you can roll your own JS client to work with this.

# Usage

- Install from pypi `wagtail-spa-integration`
- Add `wagtail_headless_preview`, and `django_filters` to INSTALLED_APPS
- Create a file in your project's directory called api.py and add the following
```
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail_spa_integration.views import SPAExtendedPagesAPIEndpoint, RedirectViewSet
from wagtail_spa_integration.headless_preview_api import PagePreviewAPIViewSet

api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint('pages', SPAExtendedPagesAPIEndpoint)
api_router.register_endpoint('page_preview', PagePreviewAPIViewSet)
api_router.register_endpoint('redirects', RedirectViewSet)
```
- Add api_router to urlpatterns in urls.py
```
from .api import api_router
...
urlpatterns = [
    url(r'^api/v2/', api_router.urls),
```
- In settings.py set HEADLESS_PREVIEW_CLIENT_URLS, see [wagtail-headless-preview](https://github.com/torchbox/wagtail-headless-preview#setup). Example:
```
HEADLESS_PREVIEW_CLIENT_URLS = {
    'default': 'http://localhost:3000/preview',
}
```


## Multiple wagtail sites

Wagtail itself can support a base API url and multiple "sites" For example:

- api.example.com is the default site where wagtail runs
- burkesoftware.com is one site served by wagtail
- passit.io is another site served by the same wagtail instance

This set up would require multiple Wagtail Sites and each Site needs it's own page.

- api.example.com's page should be a child of the wagtail root page and be set as the default Site.
- burkesoftware.com's Homepage should be a child of the api.example.com page and have a Site.
- passit.io's Homepage should be a child of the api.example.com page page and should have a Site.

`WAGTAILAPI_BASE_URL` must be set in settings.py so that the API shows the correct `detail_url` in the API.

### Sitemap support

If may be useful to explicitly request a sitemap.xml for a specific site. `from wagtail_spa_integration.views import sitemap` adds a query parameter `site` for this. Use it exactly as you would wagtail's sitemap. Then add a query parameter like `example.com/sitemap.xml?site=2`.

## Usage with Angular

Follow instructions on [Angular-Wagtail](https://gitlab.com/thelabnyc/angular-wagtail).

## Usage with NextJS

See [nextjs-wagtail](https://gitlab.com/thelabnyc/nextjs-wagtail).

## Usage with rolling your own JS

Review the angular-wagtail project and reimplement it's logic. Essentially you'll need to make a page router that loads pages from the api and connects wagtail pages to your view layer. For example a wagtail page HomePage would need to be connected to a JS HomePageComponent.

It's not likely that I'll be developing other integrations, but if you make an integration for your favorite JS framework I'd be happy to note it here. Angular happens to be a good fit because we can expect certain resources to be available (Router Module, transfer state, etc). NextJS works well too because of it's support for SSR and dynamic router option.

# Development

## Test fixtures

Create fixtures with `./manage.py dumpdata --natural-foreign --indent 2 -e contenttypes -e auth.permission -e wagtailcore.groupcollectionpermission -e wagtailcore.grouppagepermission -e wagtailimages.rendition -e sessions > data.json`

Load fixtures with `./manage.py loaddata data.json`

To load test fixtures with via an API - make a POST request to `/test-fixture/`

## Publish to pypi

Submit a tag starting with the letter v such as `v2.0.0` and CI will automatically publish
