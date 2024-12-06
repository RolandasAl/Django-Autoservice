from django.contrib import admin

# Register your models here.
from .models import Automobilio_modelis, Automobilis, Paslauga,Uzsakymo_eilute,Uzsakymas,Busena

class UzsakymoEiluteInline(admin.TabularInline):
    model = Uzsakymo_eilute
    extra = 0

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilio','data','reader','terminas')
    inlines = [UzsakymoEiluteInline]

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas','automobilio_modelis','valstybinis_nr','vin_kodas')
    list_filter = ('klientas', 'automobilio_modelis')
    search_fields = ('valstybinis_nr', 'vin_kodas')
    search_help_text = "Paieška pagal valstybinų numerį arba VIN kodą"

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas','kaina')

admin.site.register(Automobilio_modelis)
admin.site.register(Automobilis,AutomobilisAdmin)
admin.site.register(Paslauga,PaslaugaAdmin)
admin.site.register(Uzsakymo_eilute)
admin.site.register(Uzsakymas,UzsakymasAdmin)
admin.site.register(Busena)


