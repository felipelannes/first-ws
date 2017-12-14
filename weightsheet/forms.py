from django import forms
from .models import ASV_Vessel, Item

class ASV_Vessel_Form(forms.ModelForm):
	Description = forms.CharField(required=False)
	#Mass = forms.FloatField(required=False)
	#LCG = forms.FloatField(required=False)
	#TCG = forms.FloatField(required=False)
	#VCG = forms.FloatField(required=False)

	class Meta:
		model = ASV_Vessel
		fields = ('ID_ASV_Vessel', 'Name', 'Description', 'Mass', 'LCG', 'TCG', 'VCG')

class Item_Form(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('ID_Item', 'ASV_Item', 'Local_Group', 'Global_Group', 'Part_Name', 'Description', 'Mass', 'LCG', 'TCG', 'VCG')
