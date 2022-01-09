from django.shortcuts import render
from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import APISSerializers
from .models import APIS
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
@api_view(['GET'])
def allData(request):
  data = APIS.objects.all().order_by('-id')
  serializer = APISSerializers(data,many=True)
  return Response(serializer.data)