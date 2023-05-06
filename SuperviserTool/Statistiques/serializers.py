from rest_framework import serializers
from .models import *

class GetMemoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryUse
        fields = '__all__'

class GetSwapDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwapUse
        fields = '__all__'