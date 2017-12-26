from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ASV_Vessel, Group_System, Item, Bounding_Box
from .forms import ASV_Vessel_Form, Group_System_Form, Item_Form, Bounding_Box_Form
from .solvers import calculate_total_mass, calculate_LCG_CoG, calculate_TCG_CoG, calculate_VCG_CoG, get_data

# Create your views here.

def homepage(request):
    return render(request, 'weightsheet/homepage.html', {})

def vessel_add(request):
    if request.method == 'POST':
        form = ASV_Vessel_Form(request.POST)
        if form.is_valid():
            if ASV_Vessel.objects.filter(ASV_Project_Number=request.POST.get('ASV_Project_Number')).exists():
                return render(request, 'weightsheet/create_project_error.html', {'ASV_Project_Number': request.POST.get('ASV_Project_Number')} )
            else:
                form.save()
                html = "/vessel/%s"%(request.POST.get('ASV_Project_Number'))
                return redirect(html)
    else:
        form = ASV_Vessel_Form()
    return render(request, 'weightsheet/vessel_add.html', {'form': form} )

def vessel_remove(request,ASV_Project_Number):
    vessel = get_object_or_404(ASV_Vessel,ASV_Project_Number=ASV_Project_Number)
    vessel.delete()
    return redirect ('/vessel/list')

def vessel_list(request):
    vessel_list = ASV_Vessel.objects.all()
    for vessel in vessel_list:
        items_list = Group_System.objects.filter(ID_ASV=vessel)
        vessel.Mass=calculate_total_mass(items_list)
        vessel.LCG=calculate_LCG_CoG(items_list)
        vessel.TCG=calculate_TCG_CoG(items_list)
        vessel.VCG=calculate_VCG_CoG(items_list)
    return render(request, 'weightsheet/vessel_list.html', {'vessel_list': vessel_list} )


def gs_add(request,ASV_Project_Number):
    vessel = get_object_or_404(ASV_Vessel, ASV_Project_Number=ASV_Project_Number)
    vessel_iterable = ASV_Vessel.objects.filter(ASV_Project_Number=ASV_Project_Number)
    gs_item=Group_System()
    for gs_id in range(100,800,100):
        data_dict={}
        data_dict["ID_ASV"]=vessel_iterable
        data_dict["ID_GS"]=gs_id
        data_dict["Mass"]=0
        data_dict["LCG"]=0
        data_dict["TCG"]=0
        data_dict["VCG"]=0
        form = Group_System_Form(data_dict)
        if form.is_valid():
            if Group_System.objects.filter(ID_ASV=vessel_iterable, ID_GS=gs_id).exists():
                gs_item = Group_System.objects.get(ID_ASV=vessel_iterable, ID_GS=gs_id)
                gs_choose=Item.objects.filter(ID_ASV=vessel_iterable, ID_GS=gs_item)
                gs_item.change_mass(calculate_total_mass(gs_choose))
                gs_item.change_LCG(calculate_LCG_CoG(gs_choose))
                gs_item.change_TCG(calculate_TCG_CoG(gs_choose))
                gs_item.change_VCG(calculate_VCG_CoG(gs_choose))
                gs_item.save()
            else:
                form.save()
    gs_list = Group_System.objects.filter(ID_ASV=vessel_iterable)
    
    form = Bounding_Box_Form()
    item_choose=[]
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

    bounding_box_date = [calculate_total_mass(item_choose), calculate_LCG_CoG(item_choose), calculate_TCG_CoG(item_choose), calculate_VCG_CoG(item_choose)]

    return render(request, 'weightsheet/gs_add.html', {'vessel': vessel, 'gs_list': gs_list, 'form': form, 'bounding_box_date': bounding_box_date} )

def gs_items(request,ASV_Project_Number,gs):
    vessel=get_object_or_404(ASV_Vessel, ASV_Project_Number=ASV_Project_Number)
    gs_choose=Item.objects.filter(ID_ASV_id=vessel, Local_Group=gs)
    
    return render(request, 'weightsheet/gs_items.html', 
        {'gs_choose': gs_choose, 'gs': gs, 'vessel': vessel} )

def all_items(request):
    all_items = Item.objects.all()
    return render(request, 'weightsheet/all_items.html', {'all_items': all_items} )

def upload(request,ASV_Project_Number):
    data = {}
    #ASV_Project_Number=None
    if "GET" == request.method:
        return redirect('/vessel/list')
    # if not GET, then proceed
    
    xls_file = request.FILES["xls_file"]
    #if file is too large, return
    if xls_file.multiple_chunks():
    	pass

    if  ASV_Project_Number!=xls_file.name.split('/')[-1].split('-')[1]:
        return render(request, 'weightsheet/upload_error.html', {'ASV_Project_Number': ASV_Project_Number, 'flag_error': True} )

    try:
        lines = get_data(xls_file)
    except:
        return render(request, 'weightsheet/upload_error.html', {'ASV_Project_Number': ASV_Project_Number, 'flag_error': False} )


    #loop over the lines and save them in db. If error , store as string and then display
    for fields in lines: 
        vessel_iterable = ASV_Vessel.objects.filter(ASV_Project_Number=fields[11])
        gs_iterable = Group_System.objects.filter(ID_GS=fields[2] , ID_ASV_id=vessel_iterable)

        data_dict = {}
        data_dict["ID_ASV"] = vessel_iterable
        data_dict["ID_GS"] = gs_iterable
        data_dict["ID_Item"] = fields[0]
        data_dict["ASV_Item"] = fields[1]
        data_dict["Local_Group"] = fields[2]
        data_dict["Global_Group"] = fields[3]
        data_dict["Part_Name"] = fields[4]
        data_dict["Description"] = fields[5]
        data_dict["Quantity"] = fields[6]
        data_dict["Mass"] = fields[7]
        data_dict["LCG"] = fields[8]
        data_dict["TCG"] = fields[9]
        data_dict["VCG"] = fields[10]

        form = Item_Form(data_dict)
        if form.is_valid():
            if Item.objects.filter(ID_ASV=vessel_iterable, ID_GS=gs_iterable, ID_Item=fields[0], Local_Group=fields[2]).exists():
                    item = Item.objects.get(ID_ASV=vessel_iterable, ID_GS=gs_iterable, ID_Item=fields[0], Local_Group=fields[2])
                    item.Description = fields[5]
                    item.Quantity = fields[6]
                    item.Mass = fields[7]
                    item.LCG = fields[8]    
                    item.TCG = fields[9]
                    item.VCG = fields[10]
                    item.save()
            else:
                    form.save()
        else:
            pass
    gs_add(request,ASV_Project_Number)
    vessel_list(request)
    return redirect('/vessel/list')

#def bounding_box(request,vessel_iterable):
    
    # item_choose=[]
    # if request.method == 'GET':
    #     for item in Item.objects.filter(ID_ASV=vessel_iterable):
    #             if float(request.GET.get('X_aft'))<=item.LCG<=float(request.GET.get('X_forward')) \
    #             and float(request.GET.get('Y_starboard'))<=item.TCG<=float(request.GET.get('Y_portside')) \
    #             and float(request.GET.get('Z_bottom'))<=item.VCG<=float(request.GET.get('Z_up')):
    #                 item_choose+=[item]
    #             else:
    #                 pass
    # else:
    #     pass
    # return item_choose