from django.urls import path

from game_list.users.views import users

urlpatterns = [
    path('', users)
]