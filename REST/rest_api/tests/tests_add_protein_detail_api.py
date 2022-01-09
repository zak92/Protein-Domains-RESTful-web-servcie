from django.test import TestCase

import json

from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from ..serializers import *


class AddProteinDetailTest(APITestCase):
   
  def tearDown(self):
    Taxonomy.objects.all().delete() 
    Protein.objects.all().delete()
    TaxonomyFactory.reset_sequence(0) # reset foreign keys
    ProteinFactory.reset_sequence(0)

# test that the request has been fulfilled and resulted in a new resource being created.
  def test_createNewProteinEntry(self):
    protein_sample = {
    "protein_id": "TEST_PROTEIN_1",
    "sequence": "DFFNPRPEAAVLSA",
    "taxonomy": {
        "taxa_id": 50007000,
        "clade": "E",
        "genus": "Ancylostoma",
        "species": "ceylanicum"
    },
    "length": 11 }
    response = self.client.post(reverse('add_protein_detail_api'), 
                                data=json.dumps(protein_sample), 
                                content_type='application/json')
    self.assertEqual(response.status_code, 201)


# test that a new resource will not be created due to missing data (user did not fill all fields)
  def test_createNewProteinEntryFailed(self):
      protein_sample_2 = {
      "protein_id": "TEST_PROTEIN_1",
      "sequence": "DFFNPRPEAAVLSA",
      "length": 11 }
      response = self.client.post(reverse('add_protein_detail_api'), 
                                  data=json.dumps(protein_sample_2), 
                                  content_type='application/json')
      self.assertEqual(response.status_code, 400)


# check if all the necessary fields are there
  def test_AddProteinDetailCorrectFields(self):
    protein_sample = {
    "protein_id": "TEST_PROTEIN_1",
    "sequence": "DFFNPRPEAAVLSA",
    "taxonomy": {
        "taxa_id": 50007000,
        "clade": "E",
        "genus": "Ancylostoma",
        "species": "ceylanicum"
    },
    "length": 11 }
    response = self.client.post(reverse('add_protein_detail_api'), 
                                data=json.dumps(protein_sample), 
                                content_type='application/json')
    # check if data is correct
    data = json.loads(response.content)
    self.assertTrue('protein_id' in data)
    self.assertTrue('sequence' in data)
    self.assertTrue('taxonomy' in data)
    self.assertTrue('length' in data)
   
# check if all the the fields contain correct values
  def test_AddProteinDetailFieldData(self):
    protein_sample = {
    "protein_id": "TEST_PROTEIN_1",
    "sequence": "DFFNPRPEAAVLSA",
    "taxonomy": {
        "taxa_id": 50007000,
        "clade": "E",
        "genus": "Ancylostoma",
        "species": "ceylanicum"
    },
    "length": 11 }
    response = self.client.post(reverse('add_protein_detail_api'), 
                                data=json.dumps(protein_sample), 
                                content_type='application/json')
    # check if data is correct
    data = json.loads(response.content)
    # print(data)
    self.assertEqual(data['protein_id'], 'TEST_PROTEIN_1')
    self.assertEqual(data['sequence'], 'DFFNPRPEAAVLSA')
    self.assertEqual(data['taxonomy'], {'taxa_id': 50007000, 'clade': 'E', 'genus': 'Ancylostoma', 'species': 'ceylanicum'})
    self.assertEqual(data['length'], 11)
   
# ###################  Serializers ######################################
class ProteinSerializerTest(APITestCase):

  AddNewProteinSerializer = None

  def setUp(self):
    self.AddNewProteinSerializer = AddNewProteinSerializer()

  def test_addNewProteinSerializerCorrectFields(self):
    data = self.AddNewProteinSerializer.data
    self.assertEqual(set(data.keys()), set(['protein_id', 'sequence', 'taxonomy', 'length']))
    
   