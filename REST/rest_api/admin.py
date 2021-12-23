from django.contrib import admin
from .models import *

# Register your models here.

class ProteinFamilyAdmin(admin.ModelAdmin):
 list_display = ('domain_id', 'domain_description')

admin.site.register(ProteinFamily, ProteinFamilyAdmin)