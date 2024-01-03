from django.urls import path

from game_list.history.views import history

urlpatterns = [
    path('', history)
]