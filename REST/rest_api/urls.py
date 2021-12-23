from django.urls import include, path
from . import views
from . import api

urlpatterns = [
   path('api/pfam/<str:pk>', api.ProteinFamilyDetail.as_view(), name='protein_family_api'), # 3
  path('api/pfams/<int:taxa_id>', api.ProteinDomainsDetail.as_view(), name='protein_family_api'), # 5
]