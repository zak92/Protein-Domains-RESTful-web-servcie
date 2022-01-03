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



from django.db.models import F


from django.db.models import Avg, Count, Min, Sum
class DomainsCoverageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Domains
    #c = Domains.objects.annotate(start=Count('start'))
    # fields that can be served and retrieved by the user
    fields = ['start', 'stop']  # remove protein
    

from rest_framework.renderers import JSONRenderer

class ProteinCoverageSerializer(serializers.ModelSerializer):
  
  #domains = DomainsCoverageSerializer(many=True)
  

  coverage = serializers.SerializerMethodField('_get_coverage')
  def _get_coverage(self, obj):
    r = getattr(obj, 'protein_id')
    s = getattr(obj, 'id')
    print("hek" , r)
   
    coverage_x = Protein.objects.filter(protein_id__exact=r).aggregate(coverage=Sum('length'))
    coverage_y = Domains.objects.filter(protein__exact=s).aggregate(coverage=Sum('start'))
    coverage_z = Domains.objects.filter(protein__exact=s).aggregate(coverage=Sum('stop'))
    print(coverage_x['coverage'])
    result = abs(coverage_y['coverage'] - coverage_z['coverage']) / coverage_x['coverage']
    print(result)
        
    return result
    #return coverage_x['coverage'], coverage_y['coverage'], coverage_z['coverage'], result

  class Meta:
    model = Protein
   
    fields = ['coverage'] # removed 'domains', 'length'
   
    lookup_field = 'protein_id'

 

  def create(self, validated_data):
    domains_data = self.initial_data.get('domains')
    
    
    protein_details = Protein(**{**validated_data,
                
                  'domains': Domains.objects.get(pk=domains_data['id'])
                })
    protein_details.save()
    
    return protein_details





# class ProteinCoverageSerializer(serializers.ModelSerializer):
  
  

 
#   class Meta:
#     model = Protein
#     # fields that can be served and retrieved by the user
#     fields = [ 'length']
   
#     lookup_field = 'protein_id'
#     def create(self, validated_data):
#       domains_data = self.initial_data.get('domains')
#       #protein_family_data = self.initial_data.get('protein_family')
      
#       protein_details = Protein(**{**validated_data,
                  
#                    'domains': Domains.objects.get(pk=domains_data['id'])
#                   })
#       protein_details.save()
      
#       return protein_details


# class DomainsCoverageSerializer(serializers.ModelSerializer):
#   protein_length = ProteinCoverageSerializer()
#   class Meta:
#     model = Domains
#     #c = Domains.objects.annotate(start=Count('start'))
#     # fields that can be served and retrieved by the user
#     fields = ['start', 'stop', 'protein', 'protein_length'] 





  # https://stackoverflow.com/questions/52473960/how-to-get-aggregation-in-django-rest-framework-inside-same-api