import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from ..models import *

from random import randint
from random import choice

# https://factoryboy.readthedocs.io/en/stable/recipes.html
# https://factoryboy.readthedocs.io/en/stable/introduction.html

# TEST FIXTURES
class TaxonomyFactory(factory.django.DjangoModelFactory):
  taxa_id = 53326
  clade = 'E'
  genus = 'Ancylostoma'
  species = 'ceylanicum'
  class Meta:
    model = Taxonomy

class ProteinFamilyFactory(factory.django.DjangoModelFactory):
  domain_id = 'PF00360'
  domain_description = 'Phytochromeregion'
  class Meta:
    model = ProteinFamily


class ProteinFactory(factory.django.DjangoModelFactory):
  protein_id = 'A0A016S8J7'
  taxonomy = factory.SubFactory(TaxonomyFactory) 
  length = 101
  sequence = 'MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA'
  class Meta:
    model = Protein

