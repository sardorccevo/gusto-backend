from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
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

# @api_view(['POST'])
# def MakeTheOrder(request):
# 	print(request.POST)
#
# 	return Response({'status': '1'})
#
@api_view(['POST'])
def MakeTheOrder(request):
    profile = Dish.objects.all()
    if request.method == "POST":
        print(request.data)
    return Response({'status': '1'})