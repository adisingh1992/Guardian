function process(pin){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
	    if(xhttp.readyState === 4 && xhttp.status === 200){
		document.getElementById(pin).src = xhttp.responseText;
	    }
	};
	xhttp.open("GET", "process.php?pin="+pin, true);
	xhttp.send();
}
