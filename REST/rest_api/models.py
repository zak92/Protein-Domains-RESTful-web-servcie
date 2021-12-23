from django.db import models

# Create your models here.

class ProteinFamily(models.Model):
  domain_id =  models.CharField(max_length=256, null=False, blank=False, primary_key=True)
  domain_description = models.CharField(max_length=256, null=False, blank=False)
  # return a strings
  def __str__(self):
    return self.domain_description
  def __str__(self):
    return self.domain_id
  


class Taxonomy(models.Model):
  taxa_id = models.IntegerField(null=False, blank=False)
  clade = models.CharField(max_length=256, null=False, blank=False)
  genus = models.CharField(max_length=256, null=False, blank=False)
  species = models.CharField(max_length=256, null=False, blank=False)
  fk_ProteinFamily = models.ForeignKey(ProteinFamily, on_delete=models.CASCADE)
   # return a strings
  def __str__(self):
    return self.clade
  def __str__(self):
    return self.genus
  def __str__(self):
    return self.species

class Protein(models.Model):
  protein_id = models.CharField(max_length=256, null=False, blank=False)
  sequence = models.CharField(max_length=40000)
  length = models.IntegerField(null=False, blank=False)
  fk_Taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE)
   # return a strings
  def __str__(self):
    return self.protein_id
  def __str__(self):
    return self.sequence
