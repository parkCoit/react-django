from django.urls import path

from gamelist.history.views import history

urlpatterns = [
    path('', history)
]