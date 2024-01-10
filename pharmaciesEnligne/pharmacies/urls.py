from django.urls import path ,include
from rest_framework import routers
from .views import MedicamentViewSet, CategorieViewSet, ClientViewSet, CommandeViewSet, PharmacienViewSet, PharmacieViewSet 


router=routers.DefaultRouter()
router.register('Medicament', MedicamentViewSet)
router.register('Client', ClientViewSet)
router.register('Pharmacie', PharmacieViewSet)
router.register('Pharmacien', PharmacienViewSet)
router.register('Catagorie', CategorieViewSet)
router.register('Commande', CommandeViewSet)

urlpatterns = [
    #path('Medicament/', MedicamentViewSet, name='Medicament-liste'),
    #path('Categorie/', CategorieListeView.as_view(), name='Categorie-liste'),
    #path('Client/', ClientListeView.as_view(), name='Clien-listet'),
    #path('Commande/', CommandeListeView.as_view(), name='Commande-liste'),
    #path('Pharmacien/', PharmacienListeView.as_view(), name='Pharmacien-liste'),
    #path('Pharmacie/', PharmacieListeView.as_view(), name='Pharmacie-liste'),
     path('', include(router.urls))
]