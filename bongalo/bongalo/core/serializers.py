from rest_framework import serializers
from .models import Space

class SpaceSerialize(serializers.Serializer):
    class Meta:
        model:Space
        fields = ("id","room","location","guests")