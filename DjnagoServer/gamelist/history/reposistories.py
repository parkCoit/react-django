from django.http import JsonResponse
from rest_framework.response import Response

from gamelist.history.models import History
from gamelist.history.serializers import HistorySerializer


class HistoryRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(HistorySerializer(History.objects.all(), many=True).data)