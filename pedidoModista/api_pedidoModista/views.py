import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions

# Create your views here.
class calcular_conversion(APIView):
    def get(self,request,*args,**kwargs):

        metros = float(request.GET.get('metros'))
        pulgadas = 39.3701

        conversion = metros * float(pulgadas)

        conversion = f'la converion de metros: {metros} (m) a pulgadas es de: {conversion} (inch)',
        return Response(conversion, status=status.HTTP_201_CREATED)