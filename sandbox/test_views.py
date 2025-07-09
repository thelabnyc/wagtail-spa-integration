from django.core import management
from django.core.management.commands import loaddata
from rest_framework import response, views


class CreateFixturesView(views.APIView):
    """View used in end to end testing to populate database with fixtures"""

    def post(self, request):
        management.call_command(loaddata.Command(), "data.json", verbosity=0)
        return response.Response()
