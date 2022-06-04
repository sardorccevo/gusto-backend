from rest_framework import serializers

from .models import *

class MenuListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dish
		# fields = "__all__"
		fields = ['name', 'image']

class DetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dish
		fields = "__all__"
		# fields = ['name', 'image']

