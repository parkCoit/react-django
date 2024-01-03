from django.http import JsonResponse
from rest_framework.response import Response

from game_list.users.models import Users
from game_list.users.serializers import UsersSerializer


class UsersRepository(object):

    def __init__(self):
        pass

    def get_all(self):
        return Response(UsersSerializer(Users.objects.all(), many=True).data)
