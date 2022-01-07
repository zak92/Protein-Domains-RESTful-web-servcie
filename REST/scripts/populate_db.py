import os
import sys
import django
import csv
from collections import defaultdict
from rest_api.models import *
import pandas as pd

sys.path.append('/Users/zak66/OneDrive/Documents/University of London/Semester 2/Advanced Web Development/Midterm/REST - API/REST')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','REST.settings')

django.setup()

# provided CSV files containing data
data_file = 'data/pfam_descriptions.csv'
data_file_2 = 'data/assignment_data_set.csv'
data_file_3 = 'data/assignment_data_sequences.csv'

# initialize appropriate data structures
protein_family = set()
taxonomy = set()
domains = set()
protein =  defaultdict(list)

# reading two of the provided csv files
data1 = pd.read_csv(data_file_2)
data2 = pd.read_csv(data_file_3)

# using merge function by setting how='left'
output2 = pd.merge(data1, data2, on='protein_id', how='left')
# after merging the two files, write to new csv file
output2.to_csv('data/merge_file_2_and_3.csv', index=False) 

# parse csv file contents into useful data structures
with open(data_file) as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=',')
 header = csv_reader.__next__()
 for row in csv_reader:
  protein_family.add((row[0], row[1]))

# new csv file with data containing the merged content
merge_file_2_and_3 ='data/merge_file_2_and_3.csv'

# read csv file
# add the data form the column to the appropriate data structure
with open(merge_file_2_and_3) as csv_file_2:
  csv_reader_2 = csv.reader(csv_file_2, delimiter=',')
  header = csv_reader_2.__next__()
  for row in csv_reader_2:
    scientific_name = row[3].split(' ')
    genus = scientific_name[0]
    species = scientific_name[1]
    taxonomy.add((row[1], row[2], genus, species))  
    domains.add((row[4], row[6], row[7], row[1], row[5], row[0]))
    protein[row[0]] = row[9:10] + row[1:2] + row[8:9]
    
# delete all data existing in these tables prior to adding new data with a script (optional)
ProteinFamily.objects.all().delete()
Taxonomy.objects.all().delete()
Protein.objects.all().delete()
Domains.objects.all().delete()
ProteinDomainLink.objects.all().delete()

# Save the data in the data structures to the appropriate model

# save data to ProteinFamily model
protein_family_rows = {}
for pfam in protein_family:
  row = ProteinFamily.objects.create(domain_id=pfam[0], domain_description=pfam[1])
  row.save()
  protein_family_rows[pfam[0]] = row

# save data to Taxonomy model
taxonomy_rows = {}
for entry in taxonomy:
  row = Taxonomy.objects.create(taxa_id=entry[0], clade=entry[1], 
                                genus=entry[2], species=entry[3])
  row.save()
  taxonomy_rows[entry[0]] = row

# save data to Protein model
protein_rows = {}
for protein_id, data in protein.items():
  row = Protein.objects.create(protein_id=protein_id, sequence=data[0], 
                               taxonomy=taxonomy_rows[data[1]], length=data[2])
  row.save()
  protein_rows[protein_id] = row

# save data to Domains model
domain_rows = {}
for entry in domains:
  row = Domains.objects.create(description=entry[0], start=entry[1], stop=entry[2], 
                              taxonomy=taxonomy_rows[entry[3]], 
                              pfam_id=protein_family_rows[entry[4]])
  row.protein.add(protein_rows[entry[5]])
  row.save()
  domain_rows[entry[0]] = row
