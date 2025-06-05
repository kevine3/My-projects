document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from submitting

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();
    let message = document.getElementById("message");

    if (username === "" || password === "") {
        message.textContent = "Please enter both username and password!";
        message.style.color = "red";
        return;
    }

    // Simulating login authentication
    if (username === "admin" && password === "password123") {
        message.textContent = "Login successful!";
        message.style.color = "green";
    } else {
        message.textContent = "Incorrect username or password.";
        message.style.color = "red";
    }
});
