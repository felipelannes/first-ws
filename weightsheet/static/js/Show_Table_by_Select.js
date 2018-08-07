function Show_Table_by_Select(value) {
		//var element = document.getElementById(element);
	    //var x = document.getElementById(value);
	    for (i = 100; i < 900; i+=100) {
	    	//var x = document.getElementById(value);
        	//var v = element.options[i].value;
        	//console.log(i)
        	if (value != i) {
        		var y = document.getElementById(i);
        		y.style.display = "none";
        		}
        	}
        var x = document.getElementById(value);
	    if (x.style.display === "none") {
	        x.style.display = "block";
	    } else {
	        x.style.display = "none";
	    }
	} 