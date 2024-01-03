from django.http import JsonResponse
from rest_framework.response import Response

from game_list.history.models import History
from game_list.history.serializers import HistorySerializer


class HistoryRepository(object):

    def __init__(self):
        pass

    def get_all(self):
            return Response(HistorySerializer(History.objects.all(), many=True).data)