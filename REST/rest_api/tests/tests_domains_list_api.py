from django.test import TestCase

import json

from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from ..serializers import *

import random

class DomainListTest(APITestCase):
  domain_list_1 = None
  good_url = ''
  bad_url = ''
  
  def setUp(self):
    
    self.domain_list_1 = DomainsFactory()
    self.good_url = reverse('domains_list_api', kwargs={'taxonomy': 55661})
    self.bad_url = '/api/pfams/X'
   

  def tearDown(self):
    Domains.objects.all().delete() 
    Taxonomy.objects.all().delete() 
    TaxonomyFactory.reset_sequence(0)
    ProteinFamily.objects.all().delete() 
    ProteinFamilyFactory.reset_sequence(0)


  #test for successful response code for Protein Detail endpoint
  def test_DomainsListResponseSuccessCode(self):
    
    response = self.client.get(self.good_url, format='json')
    # # access the response data
    response.render()
    # # test if the http code is 200
    self.assertEqual(response.status_code, 200)


  # if user send wrong protein_id - user must get 404 code
  def test_DomainsListReturnFailOnBadDomainId(self):
    response = self.client.get(self.bad_url)
    self.assertEqual(response.status_code, 404)

# # check if a list is returned
#   def test_ProteinFamilyCorrectFields(self):
#     response = self.client.get(self.good_url, format='json')
#     response.render()
#     # check if data is correct
#     data = json.loads(response.content)
#     self.assertIsInstance(data, list)
#     self.assertIsInstance(data[0], dict)
    
# #check if all the the first element in the list contain correct values

  # def test_DomainsListFieldData(self):
    
  #     response = self.client.get(self.good_url, format='json')
  #     response.render()
     
  #     data = json.loads(response.content)
     
  #     print(data)
     
      #self.assertEqual(data[0]['protein_id'][1:38], "{'id': 2, 'protein_id': 'A0A016S8J7'}")
     
    
    # serializers

class DomainListSerializerTest(APITestCase):
  domain_list_1 = None
  DomainsListSerializer = None

  def setUp(self):
    self.DomainsListSerializer = DomainsListSerializer(instance=self.domain_list_1)
    self.domain_list_1 = DomainsFactory()
    

  def tearDown(self):
    Domains.objects.all().delete() 
    Taxonomy.objects.all().delete() 
    TaxonomyFactory.reset_sequence(0)
    ProteinFamily.objects.all().delete() 
    ProteinFamilyFactory.reset_sequence(0)

  def test_DomainsListSerializerCorrectFields(self):
    data = self.DomainsListSerializer.data
    self.assertEqual(set(data.keys()), set(['pfam_id']))


    