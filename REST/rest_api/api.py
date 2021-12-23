# rest api code

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# refactoring
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework import mixins

class ProteinFamilyDetail(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

  queryset = ProteinFamily.objects.all()
  serializer_class = ProteinFamilySerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)
  def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

class ProteinDomainsDetail(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

  queryset = Taxonomy.objects.all()
  serializer_class = ProteinDomainsSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)
  def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)