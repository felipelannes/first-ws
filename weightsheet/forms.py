from django import forms
from .models import ASV_Vessel, Group_System, Item, Bounding_Box

class ASV_Vessel_Form(forms.ModelForm):
#	ASV_Project_Number = forms.CharField(max_length=4)
	Description = forms.CharField(widget=forms.Textarea,required=False,initial='This field is optional')
	#Mass = forms.FloatField(required=False)
	#LCG = forms.FloatField(required=False)
	#TCG = forms.FloatField(required=False)
	#VCG = forms.FloatField(required=False)

	
	class Meta:
		model = ASV_Vessel
		fields = ('ASV_Project_Number', 'Name', 'Description')


class Group_System_Form(forms.ModelForm):

	class Meta:
		model = Group_System
		fields = ('ID_ASV', 'ID_GS')

class Item_Form(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('ID_ASV', 'ID_GS', 'ID_Item', 'ASV_Item', 'Local_Group', 'Global_Group', 'Part_Name', 
			'Description', 'Quantity', 'Mass', 'LCG', 'TCG', 'VCG')

class Bounding_Box_Form(forms.ModelForm):

	X_aft = forms.FloatField()
	X_forward = forms.FloatField()
	Y_starboard = forms.FloatField()
	Y_portside = forms.FloatField()
	Z_bottom = forms.FloatField()
	Z_up = forms.FloatField()

	class Meta:
		model = Bounding_Box
		fields = ('X_aft', 'X_forward', 'Y_starboard', 'Y_portside', 'Z_bottom', 'Z_up')
		localized_fields = ('__all__')
