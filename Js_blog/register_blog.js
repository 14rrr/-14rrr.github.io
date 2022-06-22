// function of safeData !!!
function validate() {
	var firstname = document.getElementById("firstname").value;
	var lastname = document.getElementById("lastname").value;
	var email = document.getElementById("email").value;
	var phone = document.getElementById("phonenumber").value;
	var age = document.getElementById("age").value;
	sessionStorage.firstname = firstname;
	sessionStorage.lastname = lastname;
	sessionStorage.email = email;
	sessionStorage.phone = phone;
	sessionStorage.age = age;

	var occupationArray = document.getElementById("radio_occupation").getElementsByTagName("input");

	for (var i=0 ; i < occupationArray.length; i++) {
		if (occupationArray[i].checked == true) {
			sessionStorage.occupation = occupationArray[i].value;
		}
	}

	var coursesArray = document.getElementById("radio_select_courses").getElementsByTagName("input");

	var logicMath = document.getElementById("course_logicmath").checked;
	var python = document.getElementById("course_python").checked;
	var web = document.getElementById("course_web").checked;
	var datascience = document.getElementById("course_game").checked;
	var game = document.getElementById("course_datascience").checked;
	var ai = document.getElementById("course_ai").checked;

	sessionStorage.logicMath = logicMath;
	sessionStorage.python = python;
	sessionStorage.web = web;
	sessionStorage.datascience = datascience;
	sessionStorage.game = game;
	sessionStorage.ai = ai;

	var payment = document.getElementById("payment").value;
	sessionStorage.payment = payment;

	var error_msg = "";
	// R1
	if (firstname.match("^[A-Z a-z]{1,30}$") == null) {
		error_msg += "ERROR: First name has to contain only characters and between 1 or 30 character<br>";
	}
	
	if (lastname.match("^[A-Z a-z]{1,30}$") == null) {
		error_msg += "ERROR: Last name has to contain only characters and between 1 or 30 character<br>";
	}
	
	// R2
	if (email.match("^[a-zA-z]*@[a-z.A-Z]*$") == null) {
		error_msg += "ERROR: Email has to contain @ or '.' <br>";
	}
	
	// R3
	if (phone.match("^((/+84)|0)[0-9]{9,10}$") == null) {
		error_msg += "ERROR: Phone number has to start with +84 or 0 is between 9 or 10 digits<br>";
	}
	
	// R4
	if (age.match("^(([0-9]|([0-9][0-9])|(1[0-4][0-9]))|150)$") == null) {
		error_msg += "ERROR: Age has to contain only digits and only from 0 or 150 old <br>";
	}

	if (sessionStorage.occupation == "highschool") {
		if (parseIn(age) < 18) {
			error_msg += "Error: If highschool then age need to be less than or equal to 18<br>";
		}
	}

	if (error_msg == "") {
		return true
	} else {
		document.getElementById("error").innerHTML = error_msg;
		return false
	}
}

function prefillData() {
	if (sessionStorage.firstname != null) {
		document.getElementById("firstname").value = sessionStorage.firstname;
		document.getElementById("lastname").value = sessionStorage.lastname;	
		document.getElementById("email").value = sessionStorage.email;	
		document.getElementById("phonenumber").value = sessionStorage.phone;	
		document.getElementById("age").value = sessionStorage.age;
		switch (sessionStorage.occupation) {
			case "highschool":
				document.getElementById("highschool").checked = true;
				break;
			case "university":
				document.getElementById("university").checked = true;
				break;
			case "working":
				document.getElementById("working").checked = true;
				break;
			case "retired":
				document.getElementById("retired").checked = true;
				break;
		}
		if (sessionStorage.logicMath == "true") {
			document.getElementById("course_logicmath").checked = true;
		}
		if (sessionStorage.python == "true") {
			document.getElementById("course_python").checked = true;
		}
		if (sessionStorage.web == "true") {
			document.getElementById("course_web").checked = true;
		}
		if (sessionStorage.datascience == "true") {
			document.getElementById("course_datascience").checked = true;
		}
		if (sessionStorage.game == "true") {
			document.getElementById("course_game").checked = true;
		}
		if (sessionStorage.ai == "true") {
			document.getElementById("course_ai").checked = true;
		}

		switch (sessionStorage.payment) {
			case "none":
				document.getElementById("payment").value = "none";
				break;
			case "paypal":
				document.getElementById("payment").value = "paypal";
				break;
			case "creditcard":
				document.getElementById("payment").value = "creditcard";
				break;	
		}
	}
}

function init() {
	var regFrom = document.getElementById("registerForm");
	regFrom.onsubmit = validate;
	prefillData();
}

window.onload = init;