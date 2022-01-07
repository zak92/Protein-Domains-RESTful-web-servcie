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

class DomainsFactory(factory.django.DjangoModelFactory):
  pfam_id = factory.SubFactory(ProteinFamilyFactory) 
  taxonomy = factory.SubFactory(TaxonomyFactory) 
  description = "abc"
  start = 1
  stop = 2
  class Meta:
    model = Domains




class ProteinFactory(factory.django.DjangoModelFactory):
  protein_id = 'A0A016S8J7'
  taxonomy = factory.SubFactory(TaxonomyFactory) 
  length = 101
  sequence = 'MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA'
  class Meta:
    model = Protein

class ProteinDomainLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProteinDomainLink

    protein = factory.SubFactory(ProteinFactory)
    domains = factory.SubFactory(DomainsFactory)

class ProteinWithDomainsListFactory(ProteinFactory):
    protein = factory.RelatedFactory(
        ProteinDomainLink,
        factory_related_name='protein',
    )

class ProteinListFactory(ProteinFactory):
  #id =  factory.Iterator([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618])
  protein_id = [
    {
        "id": 2,
        "protein_id": "A0A016S8J7"
    },
    {
        "id": 3,
        "protein_id": "A0A016SK08"
    },
    {
        "id": 4,
        "protein_id": "A0A016SLU4"
    },
    {
        "id": 5,
        "protein_id": "A0A016SS41"
    },
    {
        "id": 6,
        "protein_id": "A0A016T911"
    },
    {
        "id": 7,
        "protein_id": "A0A016TEY5"
    },
    {
        "id": 8,
        "protein_id": "A0A016TQ94"
    },
    {
        "id": 9,
        "protein_id": "A0A016TTS1"
    },
    {
        "id": 10,
        "protein_id": "A0A016U0V3"
    },
    {
        "id": 11,
        "protein_id": "A0A016U557"
    },
    {
        "id": 12,
        "protein_id": "A0A016U701"
    },
    {
        "id": 13,
        "protein_id": "A0A016UJ17"
    },
    {
        "id": 14,
        "protein_id": "A0A016USI4"
    },
    {
        "id": 15,
        "protein_id": "A0A016V1B2"
    },
    {
        "id": 16,
        "protein_id": "A0A016V7D3"
    },
    {
        "id": 17,
        "protein_id": "A0A016VK28"
    },
    {
        "id": 18,
        "protein_id": "A0A016W2S6"
    },
    {
        "id": 19,
        "protein_id": "A0A016W9A4"
    },
    {
        "id": 20,
        "protein_id": "A0A016WC87"
    },
    {
        "id": 21,
        "protein_id": "A0A016WF52"
    },
    {
        "id": 22,
        "protein_id": "A0A016WMQ5"
    },
    {
        "id": 23,
        "protein_id": "A0A016WYY3"
    },
    {
        "id": 24,
        "protein_id": "A0A016WZR8"
    },
    {
        "id": 1611,
        "protein_id": "A0A0D6LJF5"
    },
    {
        "id": 1612,
        "protein_id": "A0A0D6LM05"
    },
    {
        "id": 1613,
        "protein_id": "A0A0D6LTY2"
    },
    {
        "id": 1614,
        "protein_id": "A0A0D6LUX2"
    },
    {
        "id": 1615,
        "protein_id": "A0A0D6LX61"
    },
    {
        "id": 1616,
        "protein_id": "A0A0D6M2K0"
    },
    {
        "id": 1617,
        "protein_id": "A0A0D6M3G0"
    },
    {
        "id": 1618,
        "protein_id": "A0A0D6M6X9"
    }]

  # taxonomy = factory.SubFactory(TaxonomyFactory) 
  # length = 101
  
  # class Meta:
  #   model = Protein
  #   # rename = {'protein': 'protein_id'}
  #   abstract = False
  #   #exclude = ('id', 'protein_id',)
    
class DomainsListFactory(factory.django.DjangoModelFactory):
    # pfam_id = [
    # {
    #     "id": 1711,
    #     "pfam_id": {
    #         "domain_id": "mobidb-lite",
    #         "domain_description": "disorder prediction"
    #     }
    # },
    # {
    #     "id": 2181,
    #     "pfam_id": {
    #         "domain_id": "PF00415",
    #         "domain_description": "Regulatorofchromosomecondensation(RCC1)repeat"
    #     }
    # },
    # {
    #     "id": 2400,
    #     "pfam_id": {
    #         "domain_id": "PF14260",
    #         "domain_description": "C4-typezinc-fingerofDNApolymerasedelta"
    #     }
    # },
    # {
    #     "id": 4406,
    #     "pfam_id": {
    #         "domain_id": "PF07648",
    #         "domain_description": "Kazal-typeserineproteaseinhibitordomain"
    #     }
    # },
    # {
    #     "id": 4474,
    #     "pfam_id": {
    #         "domain_id": "mobidb-lite",
    #         "domain_description": "disorder prediction"
    #     }
    # },
    # {
    #     "id": 4650,
    #     "pfam_id": {
    #         "domain_id": "mobidb-lite",
    #         "domain_description": "disorder prediction"
    #     }
    # },
    # {
    #     "id": 6445,
    #     "pfam_id": {
    #         "domain_id": "mobidb-lite",
    #         "domain_description": "disorder prediction"
    #     }
    # },
    # {
    #     "id": 7654,
    #     "pfam_id": {
    #         "domain_id": "PF00041",
    #         "domain_description": "FibronectintypeIIIdomain"
    #     }
    # },
    # {
    #     "id": 8242,
    #     "pfam_id": {
    #         "domain_id": "mobidb-lite",
    #         "domain_description": "disorder prediction"
    #     }
    # },
    # {
    #     "id": 8333,
    #     "pfam_id": {
    #         "domain_id": "PF00307",
    #         "domain_description": "Calponinhomology(CH)domain"
    #     }
    # },
    # {
    #     "id": 8729,
    #     "pfam_id": {
    #         "domain_id": "PF16172",
    #         "domain_description": "DOCKN-terminus"
    #     }
    # },
    # {
    #     "id": 9075,
    #     "pfam_id": {
    #         "domain_id": "PF02141",
    #         "domain_description": "DENN(AEX-3)domain"
    #     }
    # }]
    pfam_id = factory.SubFactory(ProteinFamilyFactory) 
    taxonomy = factory.SubFactory(TaxonomyFactory) 
    
    #domains = factory.SubFactory(DomainsFactory)
    #pfam_id = factory.SubFactory(ProteinFamilyFactory)
    start = 1
    stop = 2

    class Meta:
        model = Domains
        #rename = {'pfam_id': 'domain_description'}


