from typing import Sequence
from django.db import models

# Create your models here.
class Taxonomy(models.Model):
  taxa_id = models.IntegerField(null=False, blank=False, primary_key=True)
  clade = models.CharField(max_length=256, null=False, blank=False)
  genus = models.CharField(max_length=256, null=False, blank=False)
  species = models.CharField(max_length=256, null=False, blank=False)
  def __str__(self):
    return self.clade
  def __str__(self):
    return self.genus
  def __str__(self):
    return self.species

class ProteinFamily(models.Model):
  domain_id =  models.CharField(max_length=256, null=False, blank=False, primary_key=True)
  domain_description = models.CharField(max_length=256, null=False, blank=False)
  # return a strings
  def __str__(self):
    return self.domain_description
  def __str__(self):
    return self.domain_id

class Protein(models.Model):
  protein_id = models.CharField(max_length=256, null=False, blank=False) 
  taxonomy = models.ForeignKey(Taxonomy, on_delete=models.DO_NOTHING)
  length = models.IntegerField(null=False, blank=False)
  sequence =  models.CharField(max_length=400000, null=False, blank=False)
 
   # return a strings
  def __str__(self):
    return self.protein_id


class Domains(models.Model):
  pfam_id = models.ForeignKey(ProteinFamily, on_delete=models.DO_NOTHING)
  taxonomy = models.ForeignKey(Taxonomy, on_delete=models.DO_NOTHING)
  description = models.CharField(max_length=500, null=False, blank=False)
  start = models.IntegerField(null=False, blank=False)
  stop = models.IntegerField(null=False, blank=False)
  protein = models.ManyToManyField(Protein, related_name='domains', through='ProteinDomainLink') 

  def __str__(self):
    return self.protein
  def __str__(self):
    return self.description
  def __str__(self):
    return str(self.pfam_id)
  


class ProteinDomainLink(models.Model):
  protein =  models.ForeignKey(Protein, on_delete=models.DO_NOTHING)
  domains = models.ForeignKey(Domains, on_delete=models.DO_NOTHING)
#https://www.sankalpjonna.com/learn-django/representing-foreign-key-values-in-django-serializers