from .models import ASV_Vessel, Group_System, Item
from .forms import ASV_Vessel_Form, Group_System_Form, Item_Form
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from math import isnan

def clean_items_list(items_list):
	out=[]
	for item in items_list:
		if item.Mass==999999 or item.LCG==999999 or item.TCG==999999 or item.VCG==999999:
			pass
		else:
			out+=[item]
	return out

def calculate_total_mass(items_list):
	items_list=clean_items_list(items_list)
	total_mass = 0
	for item in items_list:
		total_mass += item.Mass
	return total_mass

def calculate_LCG_CoG(items_list):
	items_list=clean_items_list(items_list)
	LCG_CoG = 0
	for item in items_list:
		LCG_CoG += item.Mass*item.LCG
	try:
		return LCG_CoG/calculate_total_mass(items_list)
	except:
		return 0

def calculate_TCG_CoG(items_list):
	items_list=clean_items_list(items_list)
	TCG_CoG = 0
	for item in items_list:
		TCG_CoG += item.Mass*item.TCG
	try:
		return TCG_CoG/calculate_total_mass(items_list)
	except:
		return 0

def calculate_VCG_CoG(items_list):
	items_list=clean_items_list(items_list)
	VCG_CoG = 0
	for item in items_list:
		VCG_CoG += item.Mass*item.VCG
	try:
		return VCG_CoG/calculate_total_mass(items_list)
	except:
		return 0

def get_data(data):
    df = pd.read_excel(data)
    Part_Name=[i for i in df['Part Name']]
    Description=['' if type(i)==float else i for i in df['Description']]
    Quantity=[999999 if isnan(i) else i for i in df['Qty']]
    Mass=[999999 if isnan(i) else i for i in df['Weight']]
    LCG=[999999 if isnan(i) else i for i in df['Xcg']]
    TCG=[999999 if isnan(i) else i for i in df['Ycg']]
    VCG=[999999 if isnan(i) else i for i in df['Zcg']]
    ID=1
    line=[]
    for i in range(len(Part_Name)):
	    try:
	        if Part_Name[i][:6]=='Mirror':
	            pass
	        elif 'REF ' in Part_Name[i]:
	            pass
	        else:
	        	PartName = Part_Name[i].split('-')

	        	# if isnan(Quantity[i]):
	         #    		Quantity[i]=0
		        # if isnan(Mass[i]):
		        # 	Mass[i]=0
		        # if isnan(LCG[i]):
		        # 	LCG[i]=0
		        # if isnan(TCG[i]):
		        # 	TCG[i]
		        # if isnan(VCG[i]):
		        # 	VCG[I]
		       	if PartName[0]=='ASV':
	            		line += [[ID]+[True]+[int(data.name.split('-')[3])]+\
		                        [int(PartName[3])]+[Part_Name[i]]+[Description[i]]+\
		                        [Quantity[i]]+[Mass[i]]+\
		                        [LCG[i]]+[TCG[i]]+\
		                        [VCG[i]]+[data.name.split('-')[1]]]
		        else:
	            		line += [[ID]+[False]+[int(data.name.split('-')[3])]+\
		                        [int(PartName[1])]+[Part_Name[i]]+[Description[i]]+\
		                        [Quantity[i]]+[Mass[i]]+\
		                        [LCG[i]]+[TCG[i]]+\
		                        [VCG[i]]+[data.name.split('-')[1]]]
		        ID+=1

	    except:
	    	pass
    return line