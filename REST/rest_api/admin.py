from django.contrib import admin
from .models import *

# Register your models here.

class ProteinFamilyAdmin(admin.ModelAdmin):
 list_display = ('domain_id', 'domain_description')

class TaxonomyAdmin(admin.ModelAdmin):
 list_display = ('taxa_id', 'clade', 'genus', 'species')

class ProteinAdmin(admin.ModelAdmin):
 list_display = ('protein_id', 'length')

# class SequenceAdmin(admin.ModelAdmin):
#  list_display = ('id', 'sequence')

admin.site.register(ProteinFamily, ProteinFamilyAdmin)
admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(Protein, ProteinAdmin)
# admin.site.register(Sequence, SequenceAdmin)