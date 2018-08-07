from .models import ASV_Vessel, Group_System, Item
from .forms import ASV_Vessel_Form, Group_System_Form, Item_Form
import numpy as np
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


def get_data_by_template(data):
	xl = pd.ExcelFile(data)
	group = {}
	for sheet in xl.sheet_names[5:13]:
		group[sheet.split("-")[0][1]+"00"] = xl.parse(sheet,usecols=[1,2,3,4,5,6,7],skiprows=[1,2,3,4,5,6,7,8,9,10,11,12],na_values='NaN')
	print (group)
	return group


def get_data_by_BOM(data):
	xl = pd.ExcelFile(data)
	group = {}
	for sheet in xl.sheet_names:
		if sheet.split("-")[0][1]=="h": pass
		else: group[sheet.split("-")[0][1]+"00"] = xl.parse(sheet)
	return group
