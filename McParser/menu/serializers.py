from rest_framework import serializers
from .models import McFoodInfo


class McFoodInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = McFoodInfo
        fields = "__all__"
