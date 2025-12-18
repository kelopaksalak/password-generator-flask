function errorMessage(message){
    window.alert(message)
}

function copyPassword() {
    var input = document.getElementById("password-output");
    if (!input || !input.value) {
        return;
    }

    // Create a temporary textarea to copy text (works across most browsers)
    const temp = document.createElement("textarea");
    temp.value = input.value;
    document.body.appendChild(temp);
    temp.select();
    temp.setSelectionRange(0, 99999); // for mobile devices

    try {
        document.execCommand("copy");
        window.alert("Password copied to clipboard!");
    } catch (err) {
        window.alert("Unable to copy password.");
    }

    document.body.removeChild(temp);
}