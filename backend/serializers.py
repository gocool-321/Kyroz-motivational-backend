from rest_framework import serializers;
from .models import APIS
class APISSerializers(serializers.ModelSerializer):
  class Meta:
    model = APIS
    fields = '__all__'