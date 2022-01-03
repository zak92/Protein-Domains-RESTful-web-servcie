from django.contrib import admin
from .models import *

# Register your models here.

class ProteinFamilyAdmin(admin.ModelAdmin):
 list_display = ('domain_id', 'domain_description')

class TaxonomyAdmin(admin.ModelAdmin):
 list_display = ('taxa_id', 'clade', 'genus', 'species')

class ProteinAdmin(admin.ModelAdmin):
 list_display = ('protein_id', 'sequence', 'taxonomy', 'length')


# class SequenceAdmin(admin.ModelAdmin):
#  list_display = ('id', 'sequence')

admin.site.register(ProteinFamily, ProteinFamilyAdmin)
admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(Protein, ProteinAdmin)
admin.site.register(Domains)

# admin.site.register(Sequence, SequenceAdmin)

#    from django.test import TestCase

# import json

# from django.urls import reverse
# from django.urls import reverse_lazy
# from rest_framework.test import APIRequestFactory
# from rest_framework.test import APITestCase

# from .model_factories import *
# from .serializers import *
# # Create your tests here.
# # https://docs.djangoproject.com/en/3.1/topics/testing/overview/

# class ProteinTest(APITestCase):
#   protein1 = None
#   protein2 = None
#   good_url = ''
#   bad_url = ''
  

#   def setUp(self):
#     # populate test database with dummy data from model_factories.py - ProteinFactory
#     self.protein1 = ProteinFactory.create(pk=1, protein_id='A0A014PQC0')
#     self.protein2 = ProteinFactory.create(pk=2, protein_id='A0A016S8J7')
#     self.good_url = reverse('protein_detail_api', kwargs={'protein_id': 'A0A014PQC0'})
#     self.bad_url = '/api/protein/X'
   

#   def tearDown(self):
#     Taxonomy.objects.all().delete() 
#     Protein.objects.all().delete()
#     TaxonomyFactory.reset_sequence(0) # reset foreign keys
#     ProteinFactory.reset_sequence(0)
  


#   # test for successful response code for Protein Detail endpoint
#   def test_ProteinDetailResponseSuccessCode(self):
#     response = self.client.get(self.good_url, format='json')
#     # access the response data
#     response.render()
#     # test if the http code is 200
#     self.assertEqual(response.status_code, 200)

#   # if user send wrong protein_id - user must get 404 code
#   def test_ProteinDetailReturnFailOnBadProteinId(self):
#     response = self.client.get(self.bad_url, format='json')
#     self.assertEqual(response.status_code, 404)