from django.shortcuts import render
from rest_framework import generics
from .models import user
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .serializer import  userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

@api_view(('GET',))
def out(request):
    queryset=user.objects.all()
    serial=userSerializer(queryset,many=True)
    data=serial.data
    return JsonResponse({"ok":True,"member":data})