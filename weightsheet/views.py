from django.shortcuts import render, redirect, get_object_or_404
#from django.utils import simplejson as json
import json as simplejson
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ASV_Vessel, Group_System, Item, Bounding_Box
from .forms import ASV_Vessel_Form, Group_System_Form, Item_Form, Bounding_Box_Form
from .solvers import calculate_total_mass, calculate_LCG_CoG, calculate_TCG_CoG, calculate_VCG_CoG, get_data_by_template, get_data_by_BOM 
import json
import pandas as pd
import os 

# Create your views here.

def homepage(request):
    return render(request, 'weightsheet/homepage.html', {})

#@login_required
def vessel_add(request):
    if request.method == 'POST':
        form = ASV_Vessel_Form(request.POST)
        if form.is_valid():
            # if ASV_Vessel.objects.filter(ASV_Project_Number=(request.POST.get('ASV_Project_Number')).upper()).exists():
            #     return render(request, 
            #                 'weightsheet/create_project_error.html', 
            #                 {'ASV_Project_Number': request.POST.get('ASV_Project_Number')} )
            # else:

            vessel = form.save()
            html = "/vessel/%s"%((request.POST.get('ASV_Project_Number')).upper())
            return redirect(html)
        else:
            return render(request, 
                            'weightsheet/create_project_error.html', 
                            {'ASV_Project_Number': request.POST.get('ASV_Project_Number')} )
    else:
        form = ASV_Vessel_Form()
    return render(request, 'weightsheet/vessel_add.html', {'form': form} )

def vessel_remove(request,ASV_Project_Number):
    vessel = get_object_or_404(ASV_Vessel,ASV_Project_Number=ASV_Project_Number)
    vessel.delete()
    return redirect ('/vessel/list')

def vessel_list(request):
    vessel_list = ASV_Vessel.objects.all()
    print (vessel_list)
    for vessel in vessel_list:
        items_list = Group_System.objects.filter(ID_ASV=vessel)
        print (items_list)
        vessel.Mass = calculate_total_mass(items_list)
        vessel.LCG = calculate_LCG_CoG(items_list)
        vessel.TCG = calculate_TCG_CoG(items_list)
        vessel.VCG = calculate_VCG_CoG(items_list)
    return render(request, 'weightsheet/vessel_list.html', {'vessel_list': vessel_list} )


def vessel(request,ASV_Project_Number):
    vessel = get_object_or_404(ASV_Vessel, ASV_Project_Number=ASV_Project_Number)
    vessel_iterable = ASV_Vessel.objects.filter(ASV_Project_Number=ASV_Project_Number)
    gs_item = Group_System()
    for gs_id in range(100,900,100):
        data_dict={}
        data_dict["ID_ASV"] = vessel_iterable
        data_dict["ID_GS"] = gs_id
        data_dict["Mass"]= 0
        data_dict["LCG"]= 0
        data_dict["TCG"]= 0
        data_dict["VCG"]= 0
        form = Group_System_Form(data_dict)
        if form.is_valid():
            if Group_System.objects.filter(ID_ASV=vessel_iterable, ID_GS=gs_id).exists():
                gs_item = Group_System.objects.get(ID_ASV=vessel_iterable, ID_GS=gs_id)
                gs_choose = Item.objects.filter(ID_ASV=vessel_iterable, ID_GS=gs_item)
                print (gs_choose)
                gs_item.Mass = calculate_total_mass(gs_choose)
                gs_item.LCG = calculate_LCG_CoG(gs_choose)
                gs_item.TCG = calculate_TCG_CoG(gs_choose)
                gs_item.VCG = calculate_VCG_CoG(gs_choose)
                gs_item.save()
            else:
                form.save()

    gs_list = Group_System.objects.filter(ID_ASV=vessel_iterable)
    
    form = Bounding_Box_Form()
    item_choose = []
    try:
        if request.method == 'GET':
            pass
        elif request.method == 'POST':
            form = Bounding_Box_Form(request.POST)
            if form.is_valid():
                pass
            for item in Item.objects.filter(ID_ASV=vessel_iterable):
                if float(request.POST.get('X_aft'))<=item.LCG<=float(request.POST.get('X_forward')) \
                and float(request.POST.get('Y_starboard'))<=item.TCG<=float(request.POST.get('Y_portside')) \
                and float(request.POST.get('Z_bottom'))<=item.VCG<=float(request.POST.get('Z_up')):
                    item_choose+=[item]
                else:
                    pass
        else:
            pass
    except:
        pass
        
    bounding_box_data = [calculate_total_mass(item_choose), 
                        calculate_LCG_CoG(item_choose), 
                        calculate_TCG_CoG(item_choose), 
                        calculate_VCG_CoG(item_choose)]

    return render(request, 
                'weightsheet/vessel.html', 
                {'vessel': vessel, 'gs_list': gs_list, 'form': form, 'bounding_box_data': bounding_box_data} )

def list_of_report(request,ASV_Project_Number):
    vessel = get_object_or_404(ASV_Vessel, ASV_Project_Number=ASV_Project_Number)
    dirname = os.path.dirname(__file__) + "//analysis//list_of_report.json"
    with open(dirname, 'r') as datafile:
        list_of_report = json.load(datafile)
    return render(request, 'weightsheet/list_of_report.html', {'vessel': vessel, 'list_of_report':list_of_report} )

def report_settings(request,ASV_Project_Number,report_id):
    vessel = get_object_or_404(ASV_Vessel, ASV_Project_Number=ASV_Project_Number)
    dirname = os.path.dirname(__file__) + "//analysis//"+report_id+".json"
    with open(dirname, 'r') as datafile:
        report = json.load(datafile)
    return render(request, 'weightsheet/report_settings.html', {'vessel': vessel, 'report':report,
                'report_id':report_id, 'report_name':report_id.replace("_"," ").title()})

class Weightsheet_Report(object):


    def report_cover(request,ASV_Project_Number,report_id):
        list_of_check_params = {a.split("=")[0][-10]:True for a in request.get_full_path().split('?')[-1].split("&")}
        print (list_of_check_params)
        return render(request, 'weightsheet/report/weightsheet/report_cover.html')

    def report_first_page(request,ASV_Project_Number,report_id):
        list_of_check_params = {a.split("=")[0][-10]:True for a in request.get_full_path().split('?')[-1].split("&")}
        print (list_of_check_params)
        return render(request, 'weightsheet/report/weightsheet/report_first_page.html')

    def report_summary(request,ASV_Project_Number,report_id):
        return render(request, 'weightsheet/report/weightsheet/report_summary.html')


    def report_content(request,ASV_Project_Number,report_id):
        list_of_check_params = {a.split("=")[0][:-9]:True for a in request.get_full_path().split('?')[-1].split("&")}
        print (list_of_check_params)
        if 'bom' in list_of_check_params: tag='bom'
        else: tag='template'
       
        vessel = get_object_or_404(ASV_Vessel, ASV_Project_Number=ASV_Project_Number)
        vessel_iterable = ASV_Vessel.objects.filter(ASV_Project_Number=ASV_Project_Number)

        #gs_iterable = Group_System.objects.filter(ID_GS=gs , ID_ASV_id=vessel_iterable)
        #print (gs_iterable)
        #gs_choose = Item.objects.filter(ID_ASV_id=vessel, ID_GS_id=gs_iterable)
        gs_list = Group_System.objects.filter(ID_ASV=vessel_iterable)
        items_gs = []
        bubble_dic={}
        for gs in gs_list:
            var = Item.objects.filter(ID_ASV_id=vessel, ID_GS_id=gs)
            items_gs+=[sorted(var, key=lambda item: item.Mass, reverse = True)]
            bubble_data=[]
            for item in var:
                bubble_data+=[{ "label": [item.Part_Name],
                                "backgroundColor": "rgba(255,221,50,0.2)",
                                "borderColor": "rgba(255,221,50,1)",
                                "data":[{"x":round(item.LCG,3),"y":round(item.VCG,3),"r":round(item.Mass/4,3)}]
                                }]
            bubble_dic[gs.ID_GS]=bubble_data
        #gs_list = [(round(gs.Mass,3),gs.LCG,gs.TCG,gs.VCG) for gs in gs_list]
        return render(request, 'weightsheet/report/weightsheet/report_content.html', 
                     {'bubble_dic':simplejson.dumps(bubble_dic),'gs_list':gs_list, 'vessel': vessel, "items_gs":items_gs ,'tag':tag, 'report_id':report_id, 'report_name':report_id.replace("_"," ").title()} )


#@login_required
def upload(request,ASV_Project_Number,tag):
    data = {}
    #ASV_Project_Number=None
    if "GET" == request.method:
        return redirect('/vessel/list')
    # if not GET, then proceed
    
    xls_file = request.FILES["xls_file"]
    #if file is too large, return
    if xls_file.multiple_chunks():
    	pass

    Project_Number = xls_file.name.split("'bubble_data':bubble_data,-")[1]


    if  ASV_Project_Number!=Project_Number:
        return render(request, 'weightsheet/upload_error.html', {'ASV_Project_Number': ASV_Project_Number, 'flag_error': True} )

    #try:
    if tag=="template":
        group_list = get_data_by_template(xls_file)
    else:
        group_list = get_data_by_BOM(xls_file)

    #except:
    #    return render(request, 'weightsheet/upload_error.html', {'ASV_Project_Number': ASV_Project_Number, 'flag_error': False} )

    #loop over the lines and save them in db. If error , store as string and then display
    vessel_iterable = ASV_Vessel.objects.filter(ASV_Project_Number=Project_Number)
    


    for ID_GS,group in enumerate(group_list):

        gs_iterable = Group_System.objects.filter(ID_GS=int(group) , ID_ASV_id=vessel_iterable)
        Item.objects.filter(ID_ASV=vessel_iterable, ID_GS=gs_iterable).delete()
 

        for index,item in group_list[group].iterrows():
            data_dict = {}
            data_dict["ID_ASV"] = vessel_iterable
            data_dict["ID_GS"] = gs_iterable
            data_dict["ID_Item"] = index
            data_dict["ASV_Item"] = True
            #if "A" in item[0].split("-"): data_dict["ASV_Item"] = True
            #else: data_dict["ASV_Item"] = False
            data_dict["Global_Group"] = int(group)
            data_dict["Part_Name"] = item[0]
            data_dict["Description"] = item[1]
            data_dict["Mass"] = item[2]
            data_dict["Quantity"] = item[3]
            data_dict["LCG"] = item[4]
            data_dict["TCG"] = item[5]
            data_dict["VCG"] = item[6]

            form = Item_Form(data_dict)
            if form.is_valid():
                get_object_or_404(ASV_Vessel,ASV_Project_Number=Project_Number).modification_date()
                form.save()
            else:
                pass

    vessel(request,ASV_Project_Number)
    vessel_list(request)
    html='/vessel/'+str(ASV_Project_Number)

    return redirect(html)