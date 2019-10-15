from rest_framework import serializers
from .models import Slot, Interview, SlotOption
from django.contrib.auth import get_user_model


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

class SlotOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotOption
        fields = '__all__'

