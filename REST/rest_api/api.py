# rest api code
from .models import *
from .serializers import *

# refactoring
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins

# Endpoint name: protein_family_api
class ProteinFamilyDetail(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):

  # select the appropriate queryset and  serializer
  queryset = ProteinFamily.objects.all()
  serializer_class = ProteinFamilySerializer
  
  # This function displays the data to the user in the browsable API interface
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)


# Endpoint name: protein_detail_api
class ProteinDetail(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

  # field that is used to perform object lookup of individual model instances
  lookup_field = 'protein_id'
  # select the appropriate queryset and  serializer
  queryset = Protein.objects.all()
  serializer_class = ProteinSerializer
  
  # This function retrieves and displays the data to the user in the browsable API interface
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)


# Endpoint name: protein_list_api
class ProteinList(generics.ListAPIView):
  # field that is used to perform object lookup of individual model instances
  lookup_field = 'taxonomy'
  # select the appropriate queryset and  serializer
  queryset = Domains.objects.all()
  serializer_class = ProteinListSerializer 

 # this function retrieves all relevant records in the database 
 # that match the taxonomy ID in the url 
  def get_queryset(self):
      # get the url path value
      taxonomy = self.kwargs['taxonomy']
      # filter using the taxonomy value
      return Protein.objects.filter(taxonomy__exact=taxonomy)
  

# Endpoint name: domains_list_api
class DomainsList(generics.ListAPIView):
   # field that is used to perform object lookup of individual model instances
  lookup_field = 'taxonomy'
  # select the appropriate queryset and  serializer
  queryset = Domains.objects.all()
  serializer_class = DomainsListSerializer   

  # this function retrieves all relevant records in the database 
  # that match the taxonomy ID in the url 
  def get_queryset(self):
      taxonomy = self.kwargs['taxonomy']
      return Domains.objects.filter(taxonomy__exact=taxonomy)


# Endpoint name: protein_coverage_api
class ProteinCoverage(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
  # field that is used to perform object lookup of individual model instances
  lookup_field = 'protein_id'
  # select the appropriate queryset and  serializer
  queryset = Protein.objects.all()
  serializer_class = ProteinCoverageSerializer  

  # This function displays the data to the user in the browsable API interface
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)


# Endpoint name: add_protein_detail_api
class AddNewProtein(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  
  # select the appropriate queryset and  serializer
  queryset = Protein.objects.all()  
  lookup_field = 'protein_id'
  serializer_class = AddNewProteinSerializer  

  # The functions below allow users to add (post) or update (put) a protein record 
  # or delete (delete) a protein record using the browsable API interface
  # def get(self, request, *args, **kwargs):
  #   return self.retrieve(request, *args, **kwargs)
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)