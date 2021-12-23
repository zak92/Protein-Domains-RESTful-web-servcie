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
    fields = ['id','taxa_id', 'clade', 'genus', 'species']  

class ProteinDomainsSerializer(serializers.ModelSerializer):
  taxonomy = TaxonomySerializer()
  class Meta:
    model = Protein
    # fields that can be served and retrieved by the user
    fields = ['id']  

    def create(self, validated_data):
      taxonomy_data = self.initial_data.get('ec')
      
      protein_domains = Protein(**{**validated_data,
                                'taxonomy': Taxonomy.objects.get(pk=taxonomy_data['id'])
                    })
      protein_domains.save()
      return protein_domains

# class OrganismProteinListSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = ProteinFamily
#     # fields that can be served and retrieved by the user
#     fields = ['id','protein_id']  
