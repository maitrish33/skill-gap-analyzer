async function analyze() {

    const role = document.getElementById("role").value;
    const skills = document.getElementById("skills").value
                    .split(",")
                    .map(s => s.trim());

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            role: role,
            skills: skills
        })
    });
   const data = await response.json();
   
    let missingText = "";
    if (data.missing_skills.length === 0) {
        missingText = "None ";
    } else {
        missingText = data.missing_skills.join(", ");
    }

    let output = `
        <h3>Score: ${data.score}%</h3>
        <p>Status: ${data.status}</p>
        <p><b>Missing Skills:</b> ${missingText}</p>
    `;

    // Suggestions
    if (data.suggestions.length > 0) {
        output += "<p><b>Improvement Suggestions:</b></p><ul>";

        data.suggestions.forEach(item => {
            output += `<li><b>${item.skill}:</b> ${item.tip}</li>`;
        });

        output += "</ul>";
    }

    document.getElementById("result").innerHTML = output;
}
function clearData() {
    document.getElementById("skills").value = "";
    document.getElementById("role").selectedIndex = 0;
    document.getElementById("result").innerHTML = "";
}
