from django.test import TestCase
import json
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .model_factories import *
from ..serializers import *
import random

class ProteinListTest(APITestCase):
  protein_list_1 = None
  good_url = ''
  bad_url = ''
  
  def setUp(self):
    self.good_url = reverse('protein_list_api', kwargs={'taxonomy': 53326})
    self.bad_url = '/api/proteins/X'
    self.protein_list_1 = ProteinListFactory()
   
  def tearDown(self):
    Protein.objects.all().delete()
    ProteinFactory.reset_sequence(0)
    Taxonomy.objects.all().delete() 
    TaxonomyFactory.reset_sequence(0)

  # test for successful response code for Protein Detail endpoint
  def test_ProteinListResponseSuccessCode(self):
    response = self.client.get(self.good_url, format='json')
    # access the response data
    response.render()
    self.assertEqual(response.status_code, 200)


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
      self.assertEqual(data[0]['protein_id'][1:38], "{'id': 2, 'protein_id': 'A0A016S8J7'}")
     
    
# ===================================  Relevant Serializer Tests ===============================================

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

  # check if fields are correct
  def test_proteinListSerializerCorrectFields(self):
    data = self.ProteinListSerializer.data
    self.assertEqual(set(data.keys()), set(['id', 'protein_id']))
    
  # check if field values are correct
  def test_ProteinListFieldData(self):
    data = self.ProteinListSerializer.data
    self.assertEqual(data['protein_id'][1:38], "{'id': 2, 'protein_id': 'A0A016S8J7'}")
  
 
    




  