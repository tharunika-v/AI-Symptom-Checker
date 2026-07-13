async function checkSymptom() {
    let symptom = document.getElementById("symptom").value;

    if (symptom === "") {
        document.getElementById("result").innerHTML = "Please enter a symptom.";
        return;
    }

    let response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            symptoms: symptom
        })
    });

    let data = await response.json();

    document.getElementById("result").innerHTML = data.prediction;
}
