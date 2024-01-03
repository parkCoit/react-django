from django.http import JsonResponse
from rest_framework.response import Response

from gamelist.users.models import Users
from gamelist.users.serializers import UsersSerializer


class UsersRepository(object):

    def __init__(self):
        pass

    def get_all(self):
        return Response(UsersSerializer(Users.objects.all(), many=True).data)
