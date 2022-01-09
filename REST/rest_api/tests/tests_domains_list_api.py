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
    self.good_url = reverse('domains_list_api', kwargs={'taxonomy': 55661})
    self.bad_url = '/api/pfams/X'
    self.domain_list_1 = DomainsFactory()
   

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

# ===================================  Relevant Serializer Tests ===============================================

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

  # check if fields are correct
  def test_DomainsListSerializerCorrectFields(self):
    data = self.DomainsListSerializer.data
    self.assertEqual(set(data.keys()), set(['pfam_id']))


    