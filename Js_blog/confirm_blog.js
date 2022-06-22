function loadDataAndCaculatePrice() {
	totalPrice = 0;
	var name = document.getElementById("confirm_name");
	var email = document.getElementById("confirm_email");
	var phone = document.getElementById("confirm_phonenumber");
	var age = document.getElementById("confirm_age");
	var occupation = document.getElementById("confirm_occupation");
	var courses = document.getElementById("confirm_courses")
	var payment = document.getElementById("confirm_payment");
	var total = document.getElementById("confirm_total");

	name.textContent = sessionStorage.firstname + " " + sessionStorage.lastname;
	email.textContent = sessionStorage.email;
	phone.textContent = sessionStorage.phone;
	age.textContent = sessionStorage.age;
	occupation.textContent = sessionStorage.occupation;
	
	var yourCourses = "";
	var count = 0;
	if (sessionStorage.logicMath == "true") {
		yourCourses += "logicmath, ";
		totalPrice += 449;
		count += 1;
	}
	if (sessionStorage.python == "true") {
		yourCourses += "python, ";
		totalPrice += 799;
		count += 1;
	}
	if (sessionStorage.web == "true") {
		yourCourses += "web, ";
		totalPrice += 799;
		count += 1;
	}
	if (sessionStorage.datascience == "true") {
		yourCourses += "datascience, ";
		totalPrice += 249;
		count += 1;
	}
	if (sessionStorage.game == "true") {
		yourCourses += "game, ";
		totalPrice += 149;
		count += 1;
	}
	if (sessionStorage.ai == "true") {
		yourCourses += "ai, ";
		totalPrice += 499;
		count += 1;
	}

	var discount = "";

	if (count > 2) {
		totalPrice = totalPrice * 80/100;
		discount += " (Discount 20% because you choose to by more than 3 courses)<br> ";
	}

	if (sessionStorage.occupation == "highschool") {
		totalPrice = totalPrice * 90/100;
		discount += " (Discount 10% because you are in highschool)<br> "
	}

	if (sessionStorage.payment == "paypal") {
		totalPrice = totalPrice * 105/100;
		discount += " (Increase 5% because you choose payment methods paypal)<br> "
	}

	yourCourses = yourCourses.substring(0, yourCourses.length -2);
	courses.textContent = yourCourses;
	payment.textContent = sessionStorage.payment;
	total.innerHTML = totalPrice + "VND" + discount;
}

function cancelButton() {
	window.location = "register.html";
}

function init() {
	loadDataAndCaculatePrice();
	var cancel = document.getElementById("cancelButton");
	cancel.onclick = cancelButton;
}

window.onload = init;