from rest_framework import serializers
from wagtail.contrib.redirects.models import Redirect
from wagtail.models import Site


class RedirectSerializer(serializers.ModelSerializer[Redirect]):
    site: Site = serializers.SlugRelatedField(slug_field="hostname", read_only=True)

    class Meta:
        model = Redirect
        fields = ("old_path", "is_permanent", "site", "link")
