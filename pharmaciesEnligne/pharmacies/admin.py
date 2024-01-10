
# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import*

admin.site.register(Medicament)

admin.site.register(Categorie)

admin.site.register(Client)

admin.site.register(Commande)

admin.site.register(Pharmacien)

admin.site.register(Pharmacie)