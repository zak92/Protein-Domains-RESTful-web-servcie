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

from django.db.models import Avg, Count, Min, Sum

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


from django.db.models import Avg, Count, Min, Sum
from rest_framework.response import Response
class ProteinCoverage(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
  lookup_field = 'protein_id'
  queryset = Protein.objects.all()
  serializer_class = ProteinCoverageSerializer  
  # serializer_class = CoverageSerializer 
  # pubs = Protein.objects.annotate(start=Count('start'))
  # print(pubs)
  print(serializer_class[0])
  def get(self, request, *args, **kwargs):
    # print("gdugwudg")
    return self.retrieve(request, *args, **kwargs)


  #Protein.objects.annotate(Count('length'))
  # def get_queryset(self):
        
  #       return Protein.objects.annotate(
  #           Count('domains'),
            
  #       )
 
# https://stackoverflow.com/questions/31920853/aggregate-and-other-annotated-fields-in-django-rest-framework-serializers
  
# https://stackoverflow.com/questions/43594195/django-sum-up-counts-in-one-query
  