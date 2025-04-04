document.addEventListener("DOMContentLoaded", function() {
    // Login Validation
    function validateLogin() {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const errorMsg = document.getElementById("error-msg");

        if (username === "admin" && password === "1234") {
            document.getElementById("loginForm").classList.add("hidden");
            document.getElementById("dashboard").classList.remove("hidden");
        } else {
            errorMsg.innerText = "Invalid Username or Password!";
            errorMsg.style.color = "red";
        }
    }

    window.validateLogin = validateLogin;

    // Temperature Control
    function updateTemp() {
        const temp = document.getElementById("tempControl").value;
        document.getElementById("tempValue").innerText = temp + "°C";
    }

    window.updateTemp = updateTemp;
});
