from django.db.models import lookups
from rest_framework import serializers
from .models import *


class ProteinFamilySerializer(serializers.ModelSerializer):
  class Meta:
    model = ProteinFamily
    # fields that can be served and retrieved by the user
    fields = ['domain_id','domain_description']

class TaxonomySerializer(serializers.ModelSerializer):
  class Meta:
    model = Taxonomy
    # fields that can be served and retrieved by the user
    fields = ['taxa_id', 'clade', 'genus', 'species']  

class DomainsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Domains
    # fields that can be served and retrieved by the user
    fields = ['id', 'description', 'start', 'stop'] 
  

class DomainsListSerializer(serializers.ModelSerializer):
  
  pfam_id = ProteinFamilySerializer()

  class Meta:
    model = Domains
    # fields that can be served and retrieved by the user
    fields = ['id', 'pfam_id']

class ProteinDomainsListSerializer(serializers.ModelSerializer):
  pfam_id = ProteinFamilySerializer()
  class Meta:
    model = Domains
    # fields that can be served and retrieved by the user
    fields = ['pfam_id', 'description', 'start', 'stop']

class ProteinSerializer(serializers.ModelSerializer):
  
  taxonomy = TaxonomySerializer()
  domains = ProteinDomainsListSerializer()
  

  class Meta:
    model = Protein
    # fields that can be served and retrieved by the user
    fields = ['protein_id', 'taxonomy', 'length', 'domains']
    lookup_field = 'protein_id'
    def create(self, validated_data):
      taxonomy_data = self.initial_data.get('taxonomy'),
      domains_data = self.initial_data.get('domains')
      #protein_family_data = self.initial_data.get('protein_family')
      
      protein_details = Protein(**{**validated_data,
                  'taxonomy': Taxonomy.objects.get(pk=taxonomy_data['id']),
                   'domains': Domains.objects.get(pk=domains_data['id'])
                  #'protein_family': ProteinFamily.objects.get(pk=protein_family_data['domain_id']),
                  })
      protein_details.save()
      return protein_details






class ProteinListSerializer(serializers.ModelSerializer):
  
  # protein = ProteinSerializer()

  class Meta:
    model = Protein
    # fields that can be served and retrieved by the user
    fields = ['id', 'protein_id']
    # def get_queryset(self):
    #   """
    #   This view should return a list of all the purchases
    #   for the currently authenticated user.
    #   """
      
    #   taxonomy = self.request.query_params.get('taxonomy') 
    #   return Domains.objects.filter(taxonomy=taxonomy)


    # def create(self, validated_data, *args, **kwargs):
    #   taxonomy = kwargs.get('taxonomy')
    #   return Domains.objects.filter(taxonomy=taxonomy)

    # def create(self, validated_data):
    #   protein_data = self.initial_data.get('protein'),
      # domains_data = self.initial_data.get('domains')
      #protein_family_data = self.initial_data.get('protein_family')
      
    #   protein_list = Domains(**{**validated_data,
    #               'protein': Taxonomy.objects.get(pk=protein_data['protein_id']),
    #               # 'domains': Domains.objects.get(pk=domains_data['id'])
    #               #'protein_family': ProteinFamily.objects.get(pk=protein_family_data['domain_id']),
    #               })
    #   protein_list.save()
    #   return protein_list

    # lookup_field = 'taxonomy'

    # def get_queryset(self):
    #   """
    #   This view should return a list of all the purchases
    #   for the currently authenticated user.
    #   """
    #   taxonomy = self.kwargs['taxonomy']
    #   return Domains.objects.filter(taxonomy__exact=taxonomy)
    # def get_context_data(self, **kwargs):
    #   # context = super().get_context_data(**kwargs)
    #   taxonomy = self.kwargs['taxonomy']
    #   return Domains.objects.filter(taxonomy__exact=taxonomy)
    #   # return context



   
# django rest filter instrall

# https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html  https://django-url-filter.readthedocs.io/en/latest/
# https://www.youtube.com/watch?v=3Qdy-FvUEcY