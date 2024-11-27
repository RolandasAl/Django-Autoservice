from django.contrib import admin

# Register your models here.
from .models import Automobilio_modelis, Automobilis, Paslauga,Uzsakymo_eilute,Uzsakymas

admin.site.register(Automobilio_modelis)
admin.site.register(Automobilis)
admin.site.register(Paslauga)
admin.site.register(Uzsakymo_eilute)
admin.site.register(Uzsakymas)