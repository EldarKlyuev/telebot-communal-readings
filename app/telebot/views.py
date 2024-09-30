from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from telebot.serializers import ZipSerializer


class ShkolnyaAPIView(APIView):
    def post(self, request):
        serializer = ZipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(status=status.HTTP_200_OK)
