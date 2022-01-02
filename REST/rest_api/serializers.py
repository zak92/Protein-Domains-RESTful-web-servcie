from django.db.models import lookups
from rest_framework import serializers
from .models import *
from rest_framework import parsers

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
  domains = ProteinDomainsListSerializer(many=True)
  # domains = DomainsSerializer()

  class Meta:
    model = Protein
    # fields that can be served and retrieved by the user
    fields = ['protein_id', 'sequence', 'taxonomy', 'length', 'domains']
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


class DomainsCoverageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Domains
    # fields that can be served and retrieved by the user
    fields = ['start', 'stop']
 

    

class ProteinCoverageSerializer(serializers.ModelSerializer):
  
  domains = DomainsCoverageSerializer(many=True)
 
  class Meta:
    model = Protein
    # fields that can be served and retrieved by the user
    fields = [ 'length', 'domains']
   
    lookup_field = 'protein_id'
    def create(self, validated_data):
      domains_data = self.initial_data.get('domains')
      #protein_family_data = self.initial_data.get('protein_family')
      
      protein_details = Protein(**{**validated_data,
                  
                   'domains': Domains.objects.get(pk=domains_data['id'])
                  #'protein_family': ProteinFamily.objects.get(pk=protein_family_data['domain_id']),
                  })
      protein_details.save()
      
      return protein_details

class CoverageSerializer(serializers.ModelSerializer):
  
  c = ProteinCoverageSerializer()
  class Meta:
    model = Protein # link table -> define in models
    # fields that can be served and retrieved by the user
    fields = ['c']
    extra_kwargs = {'coverage': {'required': False}}




    