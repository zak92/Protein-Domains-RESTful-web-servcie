from django.db.models import lookups
from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer
from django.db.models import Sum


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

  class Meta:
    model = Protein
    # fields that can be served and retrieved by the user
    fields = ['protein_id', 'sequence', 'taxonomy', 'length', 'domains']
    lookup_field = 'protein_id'

    # get data from referenced models
    def create(self, validated_data):
      taxonomy_data = self.initial_data.get('taxonomy'),
      domains_data = self.initial_data.get('domains')
      
      protein_details = Protein(**{**validated_data,
                  'taxonomy': Taxonomy.objects.get(pk=taxonomy_data['id']),
                   'domains': Domains.objects.get(pk=domains_data['id'])
                  })
      protein_details.save()
      return protein_details


class ProteinListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Protein
    # fields that can be served and retrieved by the user
    fields = ['id', 'protein_id']


class ProteinCoverageSerializer(serializers.ModelSerializer):
  #  SerializerMethodField is a read-only field that gets its value by calling a method 
  # on the serializer class it is attached to.
  coverage = serializers.SerializerMethodField('_get_coverage')

  # this function returns the coverage value for a given protein
  def _get_coverage(self, obj):
    # retrieves the value of 'protein_id' of the Protein object
    id_protein = getattr(obj, 'protein_id')
    # retrieves the value of 'id' of the Domains object
    id_domains = getattr(obj, 'id')   
   
    # get length of the protein that matches the protein_id in the url
    coverage_x = Protein.objects.filter(protein_id__exact=id_protein).values('length')
    # get values of the 'start' coordinate of the protein that matches the protein_id in the url & add the values
    # coverage_y = Domains.objects.filter(protein__exact=id_domains).aggregate(start=Sum('start'))
    coverage_y = Domains.objects.filter(protein__exact=id_domains).aggregate(Sum('start'))
    # get values of the 'stop' coordinate of the protein that matches the protein_id in the url & add the values
    coverage_z = Domains.objects.filter(protein__exact=id_domains).aggregate(Sum('stop'))
    # calculate the coverage with the provided equation : abs(sum(start)-sum(stop)) / length of protein
    try:
      result = (coverage_y['start__sum'] - coverage_z['stop__sum']) / coverage_x[0]['length']
      result = abs(result)
    except:
      result = None
    return result
    
  class Meta:
    model = Protein
    fields = ['coverage'] 
    lookup_field = 'protein_id'
  
  # get data from referenced models
  def create(self, validated_data):
    domains_data = self.initial_data.get('domains')
  
    protein_details = Protein(**{**validated_data,
                              'domains': Domains.objects.get(pk=domains_data['id'])
                })
    protein_details.save()
    return protein_details


class AddNewProteinSerializer(WritableNestedModelSerializer, 
                              serializers.ModelSerializer): 
  taxonomy = TaxonomySerializer()
  #domains =  ProteinDomainsListSerializer()

  class Meta:
    model = Protein
    # fields that the user can add data to create a new protein record
    fields = ['protein_id', 'sequence', 'taxonomy', 'length']


  