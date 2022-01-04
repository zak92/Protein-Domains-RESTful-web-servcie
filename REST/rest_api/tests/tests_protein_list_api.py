from django.test import TestCase

import json

from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from ..serializers import *

import random

# proteins = ['A0A016S8J7',
#                   'A0A016SK08',
#                   'A0A016SLU4',
#                   'A0A016SS41',
#                   'A0A016T911',
#                   'A0A016TEY5',
#                   'A0A016TQ94',
#                   'A0A016TTS1',
#                   'A0A016U0V3',
#                   'A0A016U557',
#                   'A0A016U701',
#                   'A0A016UJ17',
#                   'A0A016USI4',
#                   'A0A016V1B2',
#                   'A0A016V7D3',
#                   'A0A016VK28',
#                   'A0A016W2S6',
#                   'A0A016W9A4',
#                   'A0A016WC87',
#                   'A0A016WF52',
#                   'A0A016WMQ5',
#                   'A0A016WYY3',
#                   'A0A016WZR8',
#                   'A0A0D6LJF5',
#                   'A0A0D6LM05',
#                   'A0A0D6LTY2',
#                   'A0A0D6LUX2',
#                   'A0A0D6LX61',
#                   'A0A0D6M2K0',
#                   'A0A0D6M3G0',
#                   'A0A0D6M6X9']



class ProteinListTest(APITestCase):
  protein_list_1 = None
  good_url = ''
  bad_url = ''
  
  def setUp(self):
    #self.protein_list_1 = createProteinList()
    self.protein_list_1 = ProteinListFactory()
    #print(self.protein_list_1)
     #self.protein_list_1 = proteins works but not with response.status http code
    self.good_url = reverse('protein_list_api', kwargs={'taxonomy': 53326})
    self.bad_url = '/api/proteins/X'
   

  def tearDown(self):
    Protein.objects.all().delete()
    ProteinFactory.reset_sequence(0)
    Taxonomy.objects.all().delete() 
    TaxonomyFactory.reset_sequence(0)

  # test for successful response code for Protein Detail endpoint
  def test_ProteinListResponseSuccessCode(self):
    
    response = self.client.get(self.good_url, format='json')
    # # access the response data
    response.render()
    data = json.loads(response.content)
    #print(data)
    # # test if the http code is 200
    self.assertEqual(response.status_code, 200)
    #print(len(data))
    
    #self.assertEqual(len(data), 31)


  # if user send wrong protein_id - user must get 404 code
  def test_ProteinFamilyReturnFailOnBadDomainId(self):
    response = self.client.get(self.bad_url)
    self.assertEqual(response.status_code, 404)

# check if a list is returned
  def test_ProteinFamilyCorrectFields(self):
    response = self.client.get(self.good_url, format='json')
    response.render()
    # check if data is correct
    data = json.loads(response.content)
    self.assertIsInstance(data, list)
    self.assertIsInstance(data[0], dict)
    
#check if all the the first element in the list contain correct values

  def test_ProteinFamilyFieldData(self):
    
      response = self.client.get(self.good_url, format='json')
      response.render()
     
      data = json.loads(response.content)
     
      #print(data)
     
      self.assertEqual(data[0]['protein_id'][1:38], "{'id': 2, 'protein_id': 'A0A016S8J7'}")
     
    
###################  Serializers ######################################
class ProteinSerializerTest(APITestCase):
  protein_list_1 = None
  ProteinListSerializer = None

  def setUp(self):
    self.protein_list_1 = ProteinListFactory()
    self.ProteinListSerializer = ProteinListSerializer(instance=self.protein_list_1)

  def tearDown(self):
    Protein.objects.all().delete()
    ProteinFactory.reset_sequence(0)
    Taxonomy.objects.all().delete() 
    TaxonomyFactory.reset_sequence(0)

  def test_proteinListSerializerCorrectFields(self):
    data = self.ProteinListSerializer.data
    self.assertEqual(set(data.keys()), set(['id', 'protein_id']))
    

  def test_ProteinListFieldData(self):
    data = self.ProteinListSerializer.data
    
    self.assertEqual(data['protein_id'][1:38], "{'id': 2, 'protein_id': 'A0A016S8J7'}")
  
 
    




  