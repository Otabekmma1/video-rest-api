from rest_framework import serializers
from .models import *


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DowloandVideo
        fields = ['id', 'file']