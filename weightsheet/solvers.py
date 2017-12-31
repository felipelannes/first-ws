from .models import ASV_Vessel, Group_System, Item
from .forms import ASV_Vessel_Form, Group_System_Form, Item_Form
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from math import isnan


def calculate_total_mass(items_list):
	total_mass = 0
	for item in items_list:
		total_mass += item.Mass
	return total_mass

def calculate_LCG_CoG(items_list):
	LCG_CoG = 0
	for item in items_list:
		LCG_CoG += item.Mass*item.LCG
	try:
		return LCG_CoG/calculate_total_mass(items_list)
	except:
		return 0

def calculate_TCG_CoG(items_list):
	TCG_CoG = 0
	for item in items_list:
		TCG_CoG += item.Mass*item.TCG
	try:
		return TCG_CoG/calculate_total_mass(items_list)
	except:
		return 0

def calculate_VCG_CoG(items_list):
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
    Description=[i for i in df['Description']]
    Quantity=[i for i in df['Qty']]
    Mass=[i for i in df['Weight']]
    LCG=[i for i in df['Xcg']]
    TCG=[i for i in df['Ycg']]
    VCG=[i for i in df['Zcg']]
    ID=1
    line=[]
    for i in range(len(Part_Name)):
	    try:
	        if Part_Name[i][:6]=='Mirror':
	            pass
	        elif 'REF ' in Part_Name[i]:
	            pass
	        elif isnan(Quantity[i]) or isnan(Mass[i]) or isnan(LCG[i]) or isnan(TCG[i]) or isnan(VCG[i]) :
	        	pass
	        else:
	            PartName = Part_Name[i].split('-')
	            
	            if PartName[0]=='ASV':
	            		line += [[str(ID)]+[PartName[0]]+[int(data.name.split('-')[3])]+\
		                        [int(PartName[3])]+[Part_Name[i]]+[Description[i]]+\
		                        [Quantity[i]]+[Mass[i]]+\
		                        [LCG[i]]+[TCG[i]]+\
		                        [VCG[i]]+[data.name.split('-')[1]]]
	            else:
	            		line += [[str(ID)]+[PartName[0]]+[int(data.name.split('-')[3])]+\
		                        [int(PartName[1])]+[Part_Name[i]]+[Description[i]]+\
		                        [Quantity[i]]+[Mass[i]]+\
		                        [LCG[i]]+[TCG[i]]+\
		                        [VCG[i]]+[data.name.split('-')[1]]]
		            
	            ID+=1
	    except:
	    	pass
    return line