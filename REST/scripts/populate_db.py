import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append('/Users/zak66/OneDrive/Documents/University of London/Semester 2/Advanced Web Development/Midterm/REST - API/REST')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','REST.settings')
django.setup()
from rest_api.models import *

data_file = 'data/pfam_descriptions.csv'

protein_family = set()


# parse csv file contents into useful data structures
with open(data_file) as csv_file:
 csv_reader = csv.reader(csv_file, delimiter=',')
 header = csv_reader.__next__()
 for row in csv_reader:
  protein_family.add((row[0], row[1]))
 

print(len(protein_family))


# delete all data existing in these tables prior to adding new data with a script (optional)
ProteinFamily.objects.all().delete()

protein_family_rows = {}
for pfam in protein_family:
  row = ProteinFamily.objects.create(domain_id=pfam[0], domain_description=pfam[1])
  row.save()
  protein_family_rows[pfam[0]] = row