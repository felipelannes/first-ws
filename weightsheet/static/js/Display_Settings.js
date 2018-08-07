function Display_Settings(id_content) {
		var x = document.getElementById("Cover_Report");   
	    x.style.display = "none";
	    var x = document.getElementById("First_Page_Report");   
	    x.style.display = "none";
	    var x = document.getElementById("Summary_Report");   
	    x.style.display = "none";
	    var x = document.getElementById("Content_Report");   
	    x.style.display = "none";
	    var x = document.getElementById(id_content);   
	    x.style.display = "block";
	} 