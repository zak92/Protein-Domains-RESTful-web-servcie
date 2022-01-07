from django.test import TestCase

import json

from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from ..serializers import *
# Create your tests here.
# https://docs.djangoproject.com/en/3.1/topics/testing/overview/


class ProteinDetailTest(APITestCase):
  protein1 = None
  good_url = ''
  bad_url = ''
  

  def setUp(self):
    # populate test database with dummy data from model_factories.py - ProteinFactory
    self.protein1 = ProteinFactory.create(pk=1, protein_id='A0A016S8J7')
    self.good_url = reverse('protein_detail_api', kwargs={'protein_id': 'A0A016S8J7'})
    self.bad_url = '/api/protein/X'
   

  def tearDown(self):
    Taxonomy.objects.all().delete() 
    Protein.objects.all().delete()
    TaxonomyFactory.reset_sequence(0) # reset foreign keys
    ProteinFactory.reset_sequence(0)

  # test for successful response code for Protein Detail endpoint
  def test_ProteinDetailResponseSuccessCode(self):
    response = self.client.get(self.good_url, format='json')
    # access the response data
    response.render()
    # test if the http code is 200
    self.assertEqual(response.status_code, 200)



  # if user send wrong protein_id - user must get 404 code
  def test_ProteinDetailReturnFailOnBadProteinId(self):
    response = self.client.get(self.bad_url, format='json')
    self.assertEqual(response.status_code, 404)

# check if all the necessary fields are there
  def test_ProteinDetailCorrectFields(self):
    response = self.client.get(self.good_url, format='json')
    response.render() 
    # check if data is correct
    data = json.loads(response.content)
    self.assertTrue('protein_id' in data)
    self.assertTrue('sequence' in data)
    self.assertTrue('taxonomy' in data)
    self.assertTrue('length' in data)  #??????????? domains ??????????
   
# check if all the the fields contain correct values
  def test_ProteinDetailFieldData(self):
    response = self.client.get(self.good_url, format='json')
    response.render()
    # check if data is correct
    data = json.loads(response.content)
    # print(data)
    self.assertEqual(data['protein_id'], 'A0A016S8J7')
    self.assertEqual(data['sequence'], 'MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA')
    self.assertEqual(data['taxonomy'], { 'taxa_id': 53326,
                                        'clade': 'E',
                                        'genus': 'Ancylostoma',
                                        'species': 'ceylanicum'})
    self.assertEqual(data['length'], 101)
   
###################  Serializers ######################################
class ProteinSerializerTest(APITestCase):
  protein1 = None
  ProteinSerializer = None

  def setUp(self):
    self.protein1 = ProteinFactory.create(pk=1, protein_id='A0A016S8J7')
    self.ProteinSerializer = ProteinSerializer(instance=self.protein1)

  def tearDown(self):
    Taxonomy.objects.all().delete() 
    Protein.objects.all().delete()
    TaxonomyFactory.reset_sequence(0) # reset foreign keys
    ProteinFactory.reset_sequence(0)

  def test_proteinSerializerCorrectFields(self):
    data = self.ProteinSerializer.data
    self.assertEqual(set(data.keys()), set(['protein_id', 'sequence', 'taxonomy', 'length', 'domains']))
    

  def test_ProteinDetailFieldData(self):
    data = self.ProteinSerializer.data
    self.assertEqual(data['protein_id'], 'A0A016S8J7')
    self.assertEqual(data['sequence'], 'MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA')
    self.assertEqual(data['taxonomy'], { 'taxa_id': 53326,
                                        'clade': 'E',
                                        'genus': 'Ancylostoma',
                                        'species': 'ceylanicum'})
    self.assertEqual(data['length'], 101)  # domains ????????????????????
    



    # post method = https://www.youtube.com/watch?v=0EmvB9fvmsA

    # lists - https://medium.com/@stevelukis/using-listapiview-unit-test-in-django-rest-framework-5af231ce246