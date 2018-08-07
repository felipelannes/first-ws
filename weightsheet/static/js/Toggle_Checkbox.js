function Toggle_Checkbox(checkbox,attribute,unique) {
	checkbox.name = checkbox.name.toLowerCase().split(" ").join("_");
	console.log(attribute);
	if ( unique == true) {
		for (j in attribute){
			var x = document.getElementsByName(attribute[j].toLowerCase().split(" ").join("_")+"_checkbox");
			for (var i = 0; i < x.length; i++) {
			    if (x[i].type == "checkbox") {
			        x[i].checked = false;
			    }
}
	        }
	    checkbox.checked = true;
	}
}

