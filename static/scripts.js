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
function getValidation() {
	// Make request to server
	// if validated
	//	return true;
	// else
	//	return false;
}