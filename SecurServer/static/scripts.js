// General Functions

// Login Page: login.html
function submitCredentials() {
	// Get User Data
	var user = document.forms["loginForm"]["user"].value;
	var pass = document.forms["loginForm"]["pass"].value;
	var alertmsg = "";
	var sendalert = false;
	// Check User Data
	if (user.length < 1) {
		alertmsg += "No Username Entered\n"
		sendalert = true;
	}
	if (pass.length < 1) {
		alertmsg += "No Password Entered\n"
		sendalert = true;
	}
	// Respond to User Data
	if (sendalert) { // Inform the User of a Problem with the Entered Data
		alert(alertmsg);
		return false;
	} else {
		return true;
	}
}

// Access Granted Page: access.html


// Access Denied Page: access_denied.html


// Error Page: error.html


// Swipe ID Page: swipe_id.html
function getValidation(id, gps) {
	var xmlHttp = null;
	var endPoint = "http://192.168.2.2/id";
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", endPoint, false);
    xmlHttp.send({"id":id, "gps":gps});
    if (xmlHttp.responseText === "true"){
    	return true;
    }else{
    	return false;
    }
}