from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def history(request):
    print(request.data)
    return Response({'history': 'hsssh'})
