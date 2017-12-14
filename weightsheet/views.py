from django.shortcuts import render, get_object_or_404
from .models import ASV_Vessel, Item
from .forms import ASV_Vessel_Form, Item_Form
from django.shortcuts import redirect


# Create your views here.


def gs_item(request):
	gs_item = Item.objects.all()
	return render(request, 'weightsheet/gs_item.html', {'gs_item': gs_item} )

def gs_infos(request,pk):
	vessel = get_object_or_404(ASV_Vessel, pk=pk)
	return render(request, 'weightsheet/gs_infos.html', {'vessel': vessel})

def gs_add(request,pk):
    vessel = get_object_or_404(ASV_Vessel, pk=pk)
    return render(request, 'weightsheet/gs_add.html', {'vessel': vessel} )

def homepage(request):
	return render(request, 'weightsheet/homepage.html', {})

def vessel_add(request):
	if request.method == 'POST':
		form = ASV_Vessel_Form(request.POST)
		if form.is_valid():
			vessel = form.save()
			return gs_add(request, pk=vessel.pk)
	form = ASV_Vessel_Form()
	return render(request, 'weightsheet/vessel_add.html', {'form': form})

def vessel_list(request):
	vessel_list = ASV_Vessel.objects.all()
	return render(request, 'weightsheet/vessel_list.html', {'vessel_list': vessel_list} )


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "weightsheet/upload_csv.html", data)
    # if not GET, then proceed
    
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
    	pass
    #if file is too large, return
    if csv_file.multiple_chunks():
    	pass

    file_data = csv_file.read().decode("utf-8")        

    lines = file_data.strip().split("\n")
    print (lines)

    #loop over the lines and save them in db. If error , store as string and then display
    for line in lines:                        
        fields = line.split(";")
        #print (fields[1])
        data_dict = {}
        data_dict["ID_Item"] = fields[0]
        data_dict["ASV_Item"] = fields[1]
        data_dict["Local_Group"] = fields[2]
        data_dict["Global_Group"] = fields[3]
        data_dict["Part_Name"] = fields[4]
        data_dict["Description"] = fields[5]
        data_dict["Mass"] = fields[6]
        data_dict["LCG"] = fields[7]
        data_dict["TCG"] = fields[8]
        data_dict["VCG"] = fields[9]
        form = Item_Form(data_dict)
        if form.is_valid():
                form.save()    
        else:
            	pass    
    return gs_item(request) 




