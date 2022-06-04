from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *

def index(request):
    return HttpResponse("Hello, World!")

class MenuListAPIView(generics.ListCreateAPIView):

	serializer_class =  MenuListSerializer
	# permission_classes = (IsAuthenticated,)
	def get_queryset(self):
		return Dish.objects.filter(type=self.request.GET['type'])

class Details(generics.ListCreateAPIView):
	serializer_class = DetailsSerializer

	def get_queryset(self):
		return Dish.objects.filter(id=self.request.GET['id'])


def MakeTheOrder(request):
		print(request.GET)

		return Response("{'status': '1'}")
