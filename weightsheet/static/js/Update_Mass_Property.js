function Update_Mass(checkbox_obj,id_gs,actual_item_mass,new_item_mass) {
        if (checkbox_obj.checked){
            var group = document.getElementById("summary").rows[id_gs/100].cells;
            group[1].innerHTML = Number(group[1].innerHTML) - actual_item_mass + (new_item_mass + 50);
        }
        else{
            var group = document.getElementById("summary").rows[id_gs/100].cells;
            group[1].innerHTML = Number(group[1].innerHTML) + actual_item_mass - (new_item_mass + 50);
        }
}

function Update_Position_Property(checkbox_mass_obj,checkbox_lcg_obj,
	id_gs,actual_item_mass,new_item_mass,actual_item_lcg,new_item_lcg) {
	
        var group = document.getElementById("summary").rows[id_gs/100].cells; 
        if (checkbox_mass_obj.checked){

            group[1].innerHTML = Number(group[1].innerHTML) - actual_item_mass + (new_item_mass + 50);
            group[2].innerHTML = Number(group[2].innerHTML) - (actual_item_mass*actual_item_lcg) + (new_item_mass + 50);

        }
        if (checkbox_lcg_obj.checked){
                var x = document.getElementById("summary").rows[id_gs/100].cells;
                x[2].innerHTML = - actual_item_mass + (new_item_mass + 50);
        }
        else{
            var x = document.getElementById("summary").rows[1].cells;
            x[1].innerHTML = Number(x[1].innerHTML) + actual_item_mass - (new_item_mass + 50);
        }
}