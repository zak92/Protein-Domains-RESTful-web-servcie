from django.urls import include, path
from . import views
from . import api

urlpatterns = [
   path('api/pfam/<str:pk>', api.ProteinFamilyDetail.as_view(), name='protein_family_api'),
   path('api/protein/<str:protein_id>', api.ProteinDetail.as_view(), name='protein_detail_api'), 
   path('api/protein/', api.AddNewProtein.as_view(), name='add_protein_detail_api'), 
   path('api/proteins/<int:taxonomy>', api.ProteinList.as_view(), name='protein_list_api'), 
   path('api/pfams/<int:taxonomy>', api.DomainsList.as_view(), name='domain_api'),
   path('api/coverage/<str:protein_id>', api.ProteinCoverage.as_view(), name='protein_coverage_api'),
   


]