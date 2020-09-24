from .models import *
from rest_framework import serializers

class FormFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFile
        fields = "__all__"