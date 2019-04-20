from wagtail.api.v2.router import WagtailAPIRouter
from wagtail_spa_integration.views import DraftPagesAPIEndpoint

api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint('pages', DraftPagesAPIEndpoint)
