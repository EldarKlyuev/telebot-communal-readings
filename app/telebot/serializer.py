from rest_framework import serializers

from telebot.models import ZipModel, ShkolnaiaModel


class ZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipModel
        fields = '__all__'


class ShkolnayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShkolnaiaModel
        fields = '__all__'