from django.urls import path ,include
from rest_framework import routers
from .views import MedicamentViewSet, CategorieViewSet, ClientViewSet, CommandeViewSet, PharmacienViewSet, PharmacieViewSet ,MedicamentPharmacieViewSet, MedicamentPharmaciePharmacienViewSet,PharmacieMedicamentsViewSet

router=routers.DefaultRouter()
router.register(r'Medicament', MedicamentViewSet)
router.register(r'Client', ClientViewSet)
router.register(r'Pharmacie', PharmacieViewSet)
router.register(r'Pharmacien', PharmacienViewSet, basename='pharmaciens')
router.register(r'Catagorie', CategorieViewSet)
router.register(r'Commande', CommandeViewSet)
router.register(r'medicaments-by-pharmacie', MedicamentPharmacieViewSet, basename='medicaments-by-pharmacie')
router.register(r'medicaments', MedicamentPharmaciePharmacienViewSet, basename='medicaments')
router.register(r'(?P<pharmacien_id>\d+)/medicaments', PharmacieMedicamentsViewSet, basename='pharmacie_medicaments')

urlpatterns = [
    #path('Medicament/', MedicamentViewSet, name='Medicament-liste'),
    #path('Categorie/', CategorieListeView.as_view(), name='Categorie-liste'),
    #path('Client/', ClientListeView.as_view(), name='Clien-listet'),
    #path('Commande/', CommandeListeView.as_view(), name='Commande-liste'),
    #path('Pharmacien/', PharmacienListeView.as_view(), name='Pharmacien-liste'),
    #path('Pharmacie/', PharmacieListeView.as_view(), name='Pharmacie-liste'),
     path('', include(router.urls)),
     
     
]