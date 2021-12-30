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
from rest_framework import viewsets

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

class ProteinDetail(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

  lookup_field = 'protein_id'
  queryset = Protein.objects.all()
  serializer_class = ProteinSerializer
  
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)
  def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

class ProteinList(
  # mixins.CreateModelMixin,
  #                 mixins.RetrieveModelMixin,
  #                 mixins.UpdateModelMixin,
  #                 mixins.DestroyModelMixin,
  #                 generics.GenericAPIView):
                   generics.ListAPIView):

  lookup_field = 'taxonomy'
  queryset = Domains.objects.all()
  serializer_class = ProteinListSerializer 

  def get_queryset(self):
      """
      This view should return a list of all the purchases
      for the currently authenticated user.
      """
      taxonomy = self.kwargs['taxonomy']
      return Protein.objects.filter(taxonomy__exact=taxonomy)
  
  # def get(self, request, *args, **kwargs):
  #     return self.retrieve(request, *args, **kwargs)

#https://docs.djangoproject.com/en/dev/topics/db/queries/

class DomainsList(generics.ListAPIView):
  lookup_field = 'taxonomy'
  queryset = Domains.objects.all()
  serializer_class = DomainsListSerializer   

  def get_queryset(self):
      """
      This view should return a list of all the purchases
      for the currently authenticated user.
      """
      taxonomy = self.kwargs['taxonomy']
      return Domains.objects.filter(taxonomy__exact=taxonomy)
  


  