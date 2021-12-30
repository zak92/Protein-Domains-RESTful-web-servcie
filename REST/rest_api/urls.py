from django.urls import include, path
from . import views
from . import api

urlpatterns = [
   path('api/pfam/<str:pk>', api.ProteinFamilyDetail.as_view(), name='protein_family_api'),
   path('api/protein/<str:protein_id>', api.ProteinDetail.as_view(), name='protein_api'), # 1  replce protein_id with pk if protein_id=pk
   path('api/proteins/<int:taxonomy>', api.ProteinList.as_view(), name='protein_list_api'), # 3
   path('api/pfams/<int:taxonomy>', api.DomainsList.as_view(), name='domain_api')


]