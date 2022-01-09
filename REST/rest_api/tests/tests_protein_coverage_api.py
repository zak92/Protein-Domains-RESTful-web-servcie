from django.test import TestCase
import json
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .model_factories import *
from ..serializers import *

class ProteinCoverageTest(APITestCase):
  protein1 = None
  good_url = ''
  bad_url = ''
  

  def setUp(self):
    # populate test database with dummy data from model_factories.py - ProteinFactory
    self.protein1 = ProteinFactory.create(protein_id='A0A016S8J7')
    self.good_url = reverse('protein_coverage_api', kwargs={'protein_id': 'A0A016S8J7'})
    self.bad_url = '/api/protein/X'
   
  def tearDown(self):
    Protein.objects.all().delete()
    ProteinFactory.reset_sequence(0)
   
  # test for successful response code for Protein Detail endpoint
  def test_ProteinCoverageResponseSuccessCode(self):
    response = self.client.get(self.good_url, format='json')
    # access the response data
    response.render()
    # test if the http code is 200
    self.assertEqual(response.status_code, 200)

  # if user send wrong protein_id - user must get 404 code
  def test_ProteinCoverageReturnFailOnBadProteinId(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

# check if all the necessary fields are there
  def test_ProteinCoverageCorrectFields(self):
    response = self.client.get(self.good_url, format='json')
    response.render() 
    # check if data is correct
    data = json.loads(response.content)
    self.assertTrue('coverage' in data)
  

# ===================================  Relevant Serializer Tests ===============================================

class ProteinCoverageSerializerTest(APITestCase):
  protein1 = None
  ProteinCoverageSerializer = None

  def setUp(self):
    self.protein1 = ProteinFactory.create(pk=1, protein_id='A0A016S8J7')
    self.ProteinCoverageSerializer = ProteinCoverageSerializer(instance=self.protein1)

  def tearDown(self):
    Protein.objects.all().delete()
    ProteinFactory.reset_sequence(0)

  # check if fields are correct
  def test_proteinCoverageSerializerCorrectFields(self):
    data = self.ProteinCoverageSerializer.data
    self.assertEqual(set(data.keys()), set(['coverage']))
    


  
    
