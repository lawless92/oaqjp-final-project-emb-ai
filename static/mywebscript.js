let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;
    const url = `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`;

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const result = JSON.parse(this.responseText);
            document.getElementById("system_response").textContent =
                JSON.stringify(result, null, 2);
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}

    