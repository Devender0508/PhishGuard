function checkURL() {
    let url = document.getElementById("urlInput").value;
    
    if (url === "") {
        alert("Please enter a URL!");
        return;
    }

    // Send URL to backend (Flask API) for checking
    fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = `Result: ${data.result}`;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error checking URL!";
    });
}
