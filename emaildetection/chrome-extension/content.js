function getEmailText() {
    const emailBody = document.querySelector("div[role='listitem']");

    if (!emailBody) return null;

    return emailBody.innerText;
}

async function checkSpam() {
    const emailText = getEmailText();
    if (!emailText) return;

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: emailText })
    });

    const data = await response.json();

    if (data.spam) {
        alert("🚨 WARNING: This email is likely SPAM");
    } else {
        console.log("Email looks safe");
    }
}

setTimeout(checkSpam, 3000);
