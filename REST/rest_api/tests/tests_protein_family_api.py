from django.test import TestCase

import json

from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from ..serializers import *

class ProteinFamilyTest(APITestCase):
  protein_family_1 = None
  good_url = ''
  bad_url = ''
  
  def setUp(self):
    # populate test database with dummy data from model_factories.py 
    self.protein_family_1 = ProteinFamilyFactory.create(pk='PF00360')
    self.good_url = reverse('protein_family_api', kwargs={'pk': 'PF00360'})
    self.bad_url = '/api/pfam/X'
   

  def tearDown(self):
    ProteinFamily.objects.all().delete()
    ProteinFamilyFactory.reset_sequence(0)

  # test for successful response code for Protein Detail endpoint
  def test_ProteinFamilyResponseSuccessCode(self):
    response = self.client.get(self.good_url, format='json')
    # access the response data
    response.render()
    # test if the http code is 200
    self.assertEqual(response.status_code, 200)


  # if user send wrong protein_id - user must get 404 code
  def test_ProteinFamilyReturnFailOnBadDomainId(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

# check if all the necessary fields are there
  def test_ProteinFamilyCorrectFields(self):
    response = self.client.get(self.good_url, format='json')
    response.render()
    # check if data is correct
    data = json.loads(response.content)
    self.assertTrue('domain_id' in data)
    self.assertTrue('domain_description' in data)
    
# check if all the the fields contain correct values
  def test_ProteinFamilyFieldData(self):
    response = self.client.get(self.good_url, format='json')
    response.render()
    # check if data is correct
    data = json.loads(response.content)
    self.assertEqual(data['domain_id'], 'PF00360')
    self.assertEqual(data['domain_description'], 'Phytochromeregion')
    

class ProteinFamilySerializerTest(APITestCase):
  protein_family_1 = None
  ProteinFamilySerializer = None

  def setUp(self):
    self.protein_family_1 = ProteinFamilyFactory.create(pk='PF00360')
    self.ProteinFamilySerializer = ProteinFamilySerializer(instance=self.protein_family_1)

  def tearDown(self):
    ProteinFamily.objects.all().delete()
    ProteinFamilyFactory.reset_sequence(0)

  def test_proteinFamilySerializerCorrectFields(self):
    data = self.ProteinFamilySerializer.data
    self.assertEqual(set(data.keys()), set(['domain_id', 'domain_description']))
    

  def test_ProteinFamilyFieldData(self):
    data = self.ProteinFamilySerializer.data
    self.assertEqual(data['domain_id'], 'PF00360')
    self.assertEqual(data['domain_description'],'Phytochromeregion')

    