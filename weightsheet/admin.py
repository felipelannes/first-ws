from django.contrib import admin
from .models import ASV_Vessel
from .models import Group_System
from .models import Item

# Register your models here.

class ASV_Vessel_Admin(admin.ModelAdmin):
	list_display=('ASV_Project_Number','Name')
	list_filter=('ASV_Project_Number',)
	ordering = ('-ASV_Project_Number',)
	search_fields = ('ASV_Project_Number','Name')

admin.site.register(ASV_Vessel,ASV_Vessel_Admin)

class Group_System_Admin(admin.ModelAdmin):
	list_display=('ID_ASV','ID_GS')
	list_filter=('ID_ASV','ID_GS')
	ordering = ('-ID_ASV',)
	search_fields = ('ID_ASV','ID_GS')

admin.site.register(Group_System,Group_System_Admin)

class Item_Admin(admin.ModelAdmin):
	list_display=('ID_ASV','ID_GS','Part_Name')
	list_filter=('ID_ASV','ID_GS')
	ordering = ('-ID_ASV',)
	search_fields = ('ID_ASV','ID_GS')

admin.site.register(Item,Item_Admin)



